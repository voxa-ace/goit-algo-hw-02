import queue

# Create queue
request_queue = queue.Queue()

# Counter for unique identifiers
request_counter = 0

# Max requests in queue
max_requests = 5

def generate_request():
    global request_counter
    request_counter += 1
    request = f"Request #{request_counter}"
    request_queue.put(request)

def process_request():
    if request_queue.empty():
        print("Queue is empty, no requests to process.")
    while not request_queue.empty():
        request = request_queue.get()
        print("Processing request:", request)

try:
    # The main loop of program
    while True:
        user_input = input("Press Enter to generate a new request, 'p' to process requests, or 'q' to quit: ")

        if user_input == 'q':
            break
        elif user_input == '':
            if request_queue.qsize() < max_requests:
                generate_request()
            else:
                print("Queue is full. Process some requests before adding new ones.")
        elif user_input == 'p':
            process_request()
        else:
            print("Invalid input. Please press Enter, 'p', or 'q'.")
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
