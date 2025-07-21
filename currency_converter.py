
import requests

def currency_converter():
    api_key = "YOUR_API_KEY"  # Replace with your actual API key from ExchangeRate-API.com
    base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

    print("Welcome to the Currency Converter!")
    print("Please note: This converter uses an external API. You need to replace 'YOUR_API_KEY' in the code with your actual API key from ExchangeRate-API.com.")

    while True:
        from_currency = input("Enter the currency to convert from (e.g., USD, EUR): ").upper()
        to_currency = input("Enter the currency to convert to (e.g., GBP, JPY): ").upper()

        try:
            amount = float(input("Enter the amount to convert: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        try:
            response = requests.get(f"{base_url}{from_currency}")
            data = response.json()

            if data["result"] == "success":
                exchange_rate = data["conversion_rates"][to_currency]
                converted_amount = amount * exchange_rate
                print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
            else:
                print(f"Error: {data["error-type"]}")
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to the API: {e}")
        except KeyError:
            print("Invalid currency code(s). Please check your input.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        another_conversion = input("Perform another conversion? (yes/no): ").lower()
        if another_conversion != 'yes':
            break

if __name__ == "__main__":
    currency_converter()
