# proxy-server-py
# Proxy Server

This repository contains a simple Python implementation of a Proxy Server. The proxy server acts as an intermediary between a client and a remote server, forwarding HTTP requests from the client to the remote server and returning the responses to the client. It also includes a basic caching mechanism to store responses from the remote server for faster subsequent access.

## How it works

The `Proxy` class is the core component of the proxy server. It is designed to handle HTTP GET requests and cache the responses for efficient handling of repeated requests for the same resource.

### Features

- Proxies HTTP GET requests to a list of remote servers.
- Implements a basic caching mechanism to store responses from the remote server.
- Supports handling multiple servers to distribute the load.

### Requirements

- Python 3.x

### Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/proxy-server.git
cd proxy-server
