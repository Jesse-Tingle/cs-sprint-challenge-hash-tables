#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ticket_cache = {}
    route = []
    for ticket in tickets:
        if ticket.source not in ticket_cache:
            ticket_cache[ticket.source] = ticket.destination

    next_source = None
    for source in ticket_cache:
        if source == "NONE":
            next_source = ticket_cache[source]
            route.append(next_source)
            break

    while route[-1] != "NONE":
        next_source = ticket_cache[next_source]
        route.append(next_source)

    return route
