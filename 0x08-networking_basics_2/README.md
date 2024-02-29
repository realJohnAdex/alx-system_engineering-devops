A TCP socket is an endpoint instance defined by an IP address and a port in the context of either a particular TCP connection or the listening state.

A port is a virtualisation identifier defining a service endpoint (as distinct from a service instance endpoint aka session identifier).

A TCP socket is not a connection, it is the endpoint of a specific connection.

There can be concurrent connections to a service endpoint, because a connection is identified by both its local and remote endpoints, allowing traffic to be routed to a specific service instance.
