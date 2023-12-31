import http.client
import time
import random
import datetime
import logging

class Proxy:
    """This class creates a proxy server."""

    def __init__(self, cache_expiry=60):
        """Initialize the proxy server."""
        self.cache = {}  # A dictionary to store the responses from the remote server.
        self.server_addresses = ['localhost:8080', 'localhost:8081']  # A list of server addresses to proxy the request to.
        self.cache_expiry = cache_expiry  # Cache expiration time in seconds
        logging.basicConfig(filename='proxy.log', level=logging.INFO)

    def proxy(self, host, port, url, method='GET'):
        """Proxy an HTTP request to the specified host and port."""
        if url in self.cache:
            """Check if the response is already in the cache."""
            timestamp, content = self.cache[url]
            current_time = time.time()
            if current_time - timestamp < self.cache_expiry:
                logging.info(f"Returning cached content for {url}")
                return content  # Return cached content if still valid.

        try:
            """If not, proxy the request to the remote server."""
            server = random.choice(self.server_addresses)  # Randomly select a server to proxy the request to.
            conn = http.client.HTTPConnection(server)  # Create a connection to the server.
            request = conn.request(method, url)  # Send the specified HTTP method request to the server.
            response = conn.getresponse()  # Get the response from the server.

            if response.status == 200:
                """If the response is successful, store the response in the cache and return it."""
                content = response.read()
                self.cache[url] = (time.time(), content)
                logging.info(f"Proxying successful for {url}")
            else:
                """If the response is not successful, return None."""
                content = None
                logging.warning(f"Proxying failed for {url}. Status code: {response.status}")

        except http.client.HTTPException as e:
            print(f"HTTPException: {e}")
            content = None
        except Exception as e:
            print(f"An error occurred: {e}")
            content = None

        finally:
            conn.close()  # Close the connection to the server.

        return content  # Return the content of the response.

def main():
    """The main function."""
    proxy_server = Proxy()  # Create a proxy server.
    target_url = input("Enter the URL to proxy: ")
    method = input("Enter the HTTP method (default is GET): ").upper() or 'GET'
    content = proxy_server.proxy('localhost', 8080, target_url, method)  # Proxy the request to the remote server.
    if content is not None:
        print(content.decode('utf-8'))  # Print the content of the response.

if __name__ == '__main__':
    """Run the main function."""
    main()
