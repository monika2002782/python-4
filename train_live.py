# ### train details

# import requests


# def get_live_train_status(trainno):
#     base_url = "https://rappid.in/apis/train.php?train_no={}".format(trainno)
#     response = requests.get(base_url)
#     data = response.json()
#     return data


# if __name__ == "__main__":
#     train_number = "16102"
#     train_status = get_live_train_status(train_number)
#     print("*****************************************************************************")
#     print("\t\tTrain Name : ",train_status["train_name"])
#     print("*****************************************************************************")
#     for station_info in train_status["data"]:


#         if station_info["is_current_station"]:
#             print("Now Station \t\t\t\t: ",station_info["station_name"])
#             print("Distance From the Starting \t: ",station_info["distance"])
#             print("Timing \t\t\t\t\t\t: ",station_info["timing"])
#             print("Delay \t\t\t\t\t\t: ",station_info["delay"])
#             print("Platform No \t\t\t\t: ",station_info["platform"])
#             print("Halt Timing \t\t\t\t: ",station_info["halt"])
#     print("*****************************************************************************")
#     print("\t\tMessage \t\t: ",train_status["message"])
#     print("\t\tMessage Updated : ",train_status["updated_time"])
#     print("*****************************************************************************")

# import requests

# def book_train_ticket():
#     # User Input
#     source_station = input("Enter the source station: ")
#     destination_station = input("Enter the destination station: ")
#     date_of_travel = input("Enter the date of travel (YYYY-MM-DD): ")
#     num_passengers = int(input("Enter the number of passengers: "))

#     # Fetch Train Details
#     url = f"https://api.example.com/trains?source={source_station}&destination={destination_station}&date={date_of_travel}"
#     response = requests.get(url)
#     train_details = response.json()

#     # Display Available Options
#     print("Available train options:")
#     for train in train_details:
#         print(f"Train: {train['name']}")
#         print(f"Departure Time: {train['departure_time']}")
#         print(f"Arrival Time: {train['arrival_time']}")
#         print(f"Available Seats: {train['available_seats']}")
#         print()

#     # User Selection
#     selected_train = input("Enter the name of the train you want to book: ")

#     # Confirm Booking
#     confirm_booking = input(f"Confirm booking for {selected_train}? (yes/no): ")
#     if confirm_booking.lower() == "yes":
#         # Payment Process
#         # Implement the payment process here
#         print("Booking confirmed. Payment processed.")

#         # Display Confirmation
#         print("Booking Details:")
#         print(f"Train: {selected_train}")
#         print(f"Date of Travel: {date_of_travel}")
#         print(f"Passengers: {num_passengers}")
#         print("Thank you for booking with us!")
#     else:
#         print("Booking canceled.")

# book_train_ticket()