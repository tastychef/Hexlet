def is_happy_ticket(ticket):
    lenght = len(ticket)
    if lenght % 2 == 0:
        q_sym = int(lenght / 2)
        t_t = [int(i) for i in list(str(ticket))]
        list(t_t)

        if sum(t_t[:q_sym]) == sum(t_t[q_sym:]):
            return True
        else:
            return False

result = is_happy_ticket("2112332112")
print(result)
