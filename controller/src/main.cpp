#include <iostream>
#include <boost/asio.hpp>
#include <boost/json.hpp>

void handle_client(boost::asio::ip::tcp::socket socket)
{
    try
    {
        // set butter of size 1024 to receive data
        // char data[1024];
        // while(true)
        for(int i; i < 1; ++i)
        {
            // init memory to all 0s
            // std::memset(data, 0, sizeof(data));
            // boost::system::error_code error;
    
            // read from the block of memory, returns 0 if error
            // boost::asio::streambuf buffer;
            // boost::asio::read_until(socket, buffer, '\n', error);
            // size_t length = socket.read_some(boost::asio::buffer(data), error);
    
            // if(error == boost::asio::error::eof)
            // {
            //     std::cout << "client disconnected.\n";
            //     break;
            // }
            // else if(error)
            // {
            //     throw boost::system::system_error(error);
            // }

            // std::istream is(&buffer);
            // std::string json_str;
            // std::getline(is, json_str); 
            
            // if(json_str.empty())
            //     continue;

            // parse request
            // expects json data
            // boost::json::value request = boost::json::parse(data);
            
            // I wonder why it has to be C-string
            // std::string command = request.as_object()["command"].as_string().c_str();

            // init json object
            boost::json::object response;
            response["message_type"] = "new_entity";

            // message type
            boost::json::object entity;
            entity["id"] = 1;
            // nest entity into response
            response["entity"] = entity;
            
            // populate position and velocity arrays
            boost::json::array positionArray;
            positionArray.push_back(0);
            positionArray.push_back(0);
            boost::json::array velocityArray;
            velocityArray.push_back(1);
            velocityArray.push_back(-1);
            
            // nest position and velocity into entity
            entity["position"] = positionArray;
            entity["velocity"] = velocityArray;
            

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
        // init io context for server (idk boost things)
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