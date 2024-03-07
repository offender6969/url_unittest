import requests

def test_atg_world_loading():
    url = "https://atg.world"
    
    print("Starting test to check ATG.world website loading...")

    try:
        response = requests.get(url, timeout=5)  

        if response.status_code == 200:
            print("Website loaded successfully (HTTP 200)")
        else:
            print(f"Website failed to load. Status code: {response.status_code}")
            return False  

    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return False  

    print("Test passed.")
    return True  

if __name__ == "__main__":
    if test_atg_world_loading():
        print("Test Passed: ATG.world website loaded successfully.")
    else:
        print("Test Failed: ATG.world website failed to load.")
