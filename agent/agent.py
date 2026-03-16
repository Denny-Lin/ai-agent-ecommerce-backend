from tools.order_tools import get_products, get_order, create_order, cancel_order


def run_agent():
    print("AI Agent started. Type 'exit' to quit.\n")

    while True:
        user_input = input("User: ")

        if user_input.lower() == "exit":
            break

        if "product" in user_input.lower():
            result = get_products()
            print("Agent:", result)

        elif "order" in user_input.lower() and "cancel" not in user_input.lower():
            order_id = user_input.split()[-1]
            result = get_order(order_id)
            print("Agent:", result)

        elif "cancel" in user_input.lower():
            order_id = user_input.split()[-1]
            result = cancel_order(order_id)
            print("Agent:", result)

        else:
            print("Agent: Sorry, I don't understand.")


if __name__ == "__main__":
    run_agent()