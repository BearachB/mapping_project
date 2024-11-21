from livereload import Server
import os

# Determine the root of the project
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Parent directory of src/
OUTPUT_DIR = os.path.join(PROJECT_DIR, "outputs")  # Path to outputs/ directory

def main():
    # Create a Livereload server
    server = Server()

    # Watch for changes in the output directory
    server.watch(os.path.join(OUTPUT_DIR, "luas_map.html"))

    # Serve the directory
    server.serve(root=OUTPUT_DIR, open_url_delay=1, port=8000)

if __name__ == "__main__":
    # Ensure the outputs directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Serving files from: {OUTPUT_DIR}")
    main()