def main():
    # Taking user input for area or power supply
    choice = input("Choose an option:\n1. Input Area in square meters\n2. Input Power Supply in kW\n")
    
    area = 0  # Initialize area variable
    power_supply = 0  # Initialize power_supply variable
    
    if choice == '1':
        area = float(input("Enter Area in square meters: "))
        panel_size = calculate_panel_size(area)
    elif choice == '2':
        power_supply = float(input("Enter Power Supply in kW: "))
        panel_size = calculate_panel_size_from_power(power_supply)
    else:
        print("Invalid choice.")
        return
    
    energy_kwh = float(input("Enter Energy in kWh: "))
    sunlight_hours = 6
    energy_wh = energy_kwh * 1000  # Convert kWh to Wh
    
    
    # Calculations
    panel_size_watts = energy_wh / sunlight_hours
    num_panels = panel_size_watts / 300
    battery_ah = max(energy_wh / 12, 200)  # Ensure battery AH is at least 200
    charge_controller_amp = panel_size_watts / 12
    inverter_va = battery_ah + (20 / 100) * battery_ah
    
    # Calculate total cost
    total_cost = (area * 6202) + 10000
    
    # Calculate earnings for government and private company
    government_earnings = (energy_kwh * 3) * 1000  # Convert to Wh
    private_company_earnings = (energy_kwh * 7) * 1000  # Convert to Wh
    
    # Convert earnings to per day, per month, and per year
    earnings_per_day_government = government_earnings / 365
    earnings_per_month_government = government_earnings / 12
    earnings_per_year_government = government_earnings
    
    earnings_per_day_private = private_company_earnings / 365
    earnings_per_month_private = private_company_earnings / 12
    earnings_per_year_private = private_company_earnings
    
    # Output results
    print("\nResults:")
    print("Panel Size: {} watts".format(panel_size_watts))
    print("Number of Panels: {:.2f}".format(num_panels))
    print("Battery: {:.2f} AH".format(battery_ah))
    print("Charge Controller: {:.2f} Amperes".format(charge_controller_amp))
    print("Inverter: {:.2f} VA".format(inverter_va))
    print("Total Cost: Rs. {:.2f}".format(total_cost))
    print("\nEarnings from Government:")
    print("Per Day: Rs. {:.2f}".format(earnings_per_day_government))
    print("Per Month: Rs. {:.2f}".format(earnings_per_month_government))
    print("Per Year: Rs. {:.2f}".format(earnings_per_year_government))
    print("\nEarnings from Private Company:")
    print("Per Day: Rs. {:.2f}".format(earnings_per_day_private))
    print("Per Month: Rs. {:.2f}".format(earnings_per_month_private))
    print("Per Year: Rs. {:.2f}".format(earnings_per_year_private))

def calculate_panel_size(area):
    return area * 150  # Assumption: 150 W/sq.m panel efficiency

def calculate_panel_size_from_power(power_supply):
    return (power_supply * 1000) / 6  # Convert kW to watts and assume 6 sunlight hours

if __name__ == "__main__":
    main()
