class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    routes = {}

    route = [None] * length

    for ticket in tickets:
        routes[ticket.source] = ticket.destination
    next_stop = routes["NONE"]

    for r in range(0, length):
        route[r] = next_stop
        next_stop = routes[next_stop]

    return route
