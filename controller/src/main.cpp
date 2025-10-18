#include <iostream>
#include <boost/asio.hpp>
#include <boost/json.hpp>

void handle_client(boost::asio::ip::tcp::socket socket)
{
    try
    {
        // set butter of size 1024 to receive data
        // init memory to all 0s
        char data[1024];
        while(true)
        {
            std::memset(data, 0, sizeof(data));
            boost::system::error_code error;
    
            // read from the block of memory, returns 0 if error
            boost::asio::streambuf buffer;
            boost::asio::read_until(socket, buffer, '\n', error);
            // size_t length = socket.read_some(boost::asio::buffer(data), error);
    
            if(error == boost::asio::error::eof)
            {
                std::cout << "client disconnected.\n";
                break;
            }
            else if(error)
            {
                throw boost::system::system_error(error);
            }

            std::istream is(&buffer);
            std::string json_str;
            std::getline(is, json_str); 
            
            if(json_str.empty())
                continue;

            // parse request
            // expects json data
            boost::json::value request = boost::json::parse(data);
            
            // I wonder why it has to be C-string
            std::string command = request.as_object()["command"].as_string().c_str();

            // logic to handle the data
            boost::json::object response;
            if(!command.empty())
            {
                boost::json::object entity;
                entity["id"] = 1;
                boost::json::array positionArray({0, 0});
                boost::json::array velocityArray({1, -1});
                entity["position"] = positionArray;
                entity["velocity"] = velocityArray;
                response["entity"] = entity;
            }
            else
            {
                response["error"] = "Not sure what's going on here.";
            }

            std::string response_str = boost::json::serialize(response) + '\n';
            std::cout << "Serialized response: " << response_str << std::endl;

            boost::asio::write(socket, boost::asio::buffer(response_str));
        }
    }
    catch(const std::exception& e)
    {
        std::cerr << "Error handling client: " << e.what() << '\n';
    }
}

int main()
{
    try
    {
        boost::asio::io_context io_context;
        
        // accept connections on default IP, port 5000
        boost::asio::ip::tcp::acceptor acceptor(io_context, boost::asio::ip::tcp::endpoint(boost::asio::ip::tcp::v4(), 5000));

        std::cout << "Listening on port 5000" << std::endl;

        while(true)
        {
            // use returned context from acceptor
            boost::asio::ip::tcp::socket socket(io_context);
            acceptor.accept(socket);

            // detach thread to keep running on OS level
            std::thread(handle_client, std::move(socket)).detach();
        }
    }
    catch(const std::exception& e)
    {
        std::cerr << "Server error: " << e.what() << '\n';
    }
    
    return 0;
}