print("BREAKER FAILURE PROTECTION SIMULATOR")

fault_current = float(input("Enter fault current (A): "))
pickup_current = float(input("Enter relay pickup current (A): "))
breaker_time = float(input("Enter breaker operating time (ms): "))
allowed_time = float(input("Enter maximum allowed clearing time (ms): "))

print("\n--- PROTECTION ANALYSIS ---")

if fault_current >= pickup_current:
    print("Fault Status       : FAULT DETECTED")

    if breaker_time <= allowed_time:
        print("Breaker Status     : SUCCESSFUL")
        print("Protection Status  : FAULT CLEARED")
    else:
        print("Breaker Status     : FAILED")
        print("Protection Status  : BACKUP TRIP INITIATED")

else:
    print("Fault Status       : NO FAULT")
    print("Breaker Status     : NORMAL")
    print("Protection Status  : SYSTEM NORMAL")
