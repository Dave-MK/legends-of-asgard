from PIL import Image
import os


def convert_and_resize_image(input_path, temp_path, output_path, scale=0.5):
    try:
        # Convert AVIF to JPG
        with Image.open(input_path) as img:
            img = img.convert("RGB")
            img.save(temp_path, "JPEG")
        
        # Resize the JPG image
        with Image.open(temp_path) as img:
            width, height = img.size
            new_width = int(width * scale)
            new_height = int(height * scale)
            resized_img = img.resize((new_width, new_height))
            
            # Convert back to AVIF
            resized_img.save(output_path, "AVIF")
            print(f"Image resized and saved to {output_path}")
        
        # Remove the temporary JPG file
        os.remove(temp_path)
    except Exception as e:
        print(f"An error occurred with {input_path}: {e}")


# List of images to process
images = [
    {
        "input": r'assets\images\gods\angraboda_prof.avif',
        "temp": r'assets\images\gods\angraboda_prof_temp.jpg',
        "output": r'assets\images\gods\angraboda_prof_rs.avif'
    },
    {
        "input": r'assets\images\gods\freyja_prof.avif',
        "temp": r'assets\images\gods\freyja_prof_temp.jpg',
        "output": r'assets\images\gods\freyja_prof_rs.avif'
    },
    {
        "input": r'assets\images\gods\freyr_prof.avif',
        "temp": r'assets\images\gods\freyr_prof_temp.jpg',
        "output": r'assets\images\gods\freyr_prof_rs.avif'
    },
    {
        "input": r'assets\images\gods\yggdrassil_prof.avif',
        "temp": r'assets\images\gods\yggdrassil_prof_temp.jpg',
        "output": r'assets\images\gods\yggdrassil_prof_rs.avif'
    },
    {
        "input": r'assets\images\gods\althing_prof.avif',
        "temp": r'assets\images\gods\althing_prof_temp.jpg',
        "output": r'assets\images\gods\althing_prof_rs.avif'
    }
    # Add more images as needed
]

# Process each image
for image in images:
    convert_and_resize_image(
        image["input"], image["temp"], image["output"]
    )