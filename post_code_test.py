'''
Created on 16 Apr 2020

@author: Louise Thomas

INSTRUCTIONS:

Postcode Lookup Tool – Code Test
At COOK, one of the things we often need to do is to lookup a postcode from our database and
return a customer’s delivery options for their postcode.
Imagine that the COOK e-commerce system has a postcode lookup class that implements the
following interface:

interface IPostcodeLookup
{
string[] GetValidDeliveryOptions(string postcode);
}

However, it is currently fairly basic and doesn’t provide the granularity of delivery options that the
business would like to provide to customers in the future. It is therefore required to rewrite this part
of the system to provide this enhanced functionality without other code needing a significant
rewrite.

Using C#, write the implementation of a new class that, given a customers full UK postcode returns
their available delivery options based on the sample dataset below. Please aim to match the most
specific version of a postcode first. Additionally, please include code to capture the raw
unvalidated user input and display the result on screen - using C# and any related tools/tech stack
as appropriate.

Sample Delivery Options Dataset
TN9 Delivery from Warehouse
TN9 1AP No Deliveries
TN8 Delivery from Warehouse
TN11 Delivery from Warehouse
TN1 Van Delivery, Collect from Tunbridge Wells
TN2 Van Delivery, Collect from Tunbridge Wells
TN10 Van Delivery
TN13 Delivery from Sevenoaks, Collect from Sevenoaks
TN14 Delivery from Sevenoaks, Collect from Sevenoaks
TN15 Collect from Sevenoaks
ME No Deliveries
ME10 Collect from Kitchen
ME10 3 Collect from Kitchen, Delivery from Sittingbourne
IV No Deliveries
All others Delivery by Courier

Sample Expected Outputs
Input Output
TN9 1AP No Deliveries
ME10 2AA Collect from Kitchen
ME10 3HH Collect from Kitchen, Delivery from Sittingbourne
ME9 1AA No Deliveries
W1N 4DJ Delivery by Courier
TN9 1AB Delivery from Warehouse
TN15 5AB Collect from Sevenoaks
TN1 2QP Van Delivery, Collect from Tunbridge Wells
'''


import sys
rc = 0

# Data dictionary of key/value delivery options by postcode.
delivery_options_dataset = {
    "TN9": "Delivery from Warehouse",
    "TN9 1AP": "No Deliveries",
    "TN8": "Delivery from Warehouse",
    "TN11": "Delivery from Warehouse",
    "TN1": ["Van Delivery", "Collect from Tunbridge Wells"],
    "TN2": ["Van Delivery", "Collect from Tunbridge Wells"],
    "TN10": "Van Delivery",
    "TN13": ["Delivery from Sevenoaks", "Collect from Sevenoaks"],
    "TN14": ["Delivery from Sevenoaks", "Collect from Sevenoaks"],
    "TN15": "Collect from Sevenoaks",
    "ME": "No Deliveries",
    "ME10": "Collect from Kitchen",
    "ME10 3": ["Collect from Kitchen", "Delivery from Sittingbourne"],
    "IV": "No Deliveries",
    "All others": "Delivery by Courier"
}

# Ask for the user to input a postcode
postcode = input("Please enter a postcode to receive delivery or collection option/s: ").upper()

# A function for checking the postcode from the user input against the key in the dictionary.
def get_delivery_option(postcode_key):
    tmp_key = postcode_key
    while tmp_key:
        delivery_option = delivery_options_dataset.get(tmp_key, None)
        if delivery_option:
            return delivery_option
        tmp_key = tmp_key[0:-1]
    return None

delivery_options = get_delivery_option(postcode)

# To check if there is a match in the key of the dictionary and the printing the result.
if delivery_options is None:
    print(f"Delivery by Courier is available for postcode: {postcode}")
elif isinstance(delivery_options, list):
    delivery_options = " or ".join(delivery_options)
    print(f"For postcode {postcode}, the delivery/collection options are: {delivery_options}")
else:
    print(f"For postcode {postcode}, the delivery/collection option is: {delivery_options}")


sys.exit(rc)
