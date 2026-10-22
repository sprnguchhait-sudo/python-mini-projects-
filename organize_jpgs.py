"""Task 3: Move JPG/JPEG images from a folder into a subfolder."""
from pathlib import Path
import shutil


def unique_destination(destination: Path) -> Path:
    """Return a non-existing path, adding a number if necessary."""
    if not destination.exists():
        return destination
    counter = 1
    while True:
        candidate = destination.with_name(f"{destination.stem}_{counter}{destination.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def main():
    raw_folder = input("Enter the folder path containing JPG files: ").strip().strip('"')
    source = Path(raw_folder).expanduser()
    if not source.is_dir():
        print("Error: that folder does not exist.")
        return

    destination_folder = source / "jpg_files"
    destination_folder.mkdir(exist_ok=True)
    moved = 0
    for file_path in source.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in {".jpg", ".jpeg"}:
            destination = unique_destination(destination_folder / file_path.name)
            shutil.move(str(file_path), str(destination))
            print(f"Moved: {file_path.name} -> {destination.name}")
            moved += 1

    print(f"Finished. Moved {moved} JPG/JPEG file(s) to: {destination_folder}")


if __name__ == "__main__":
    main()
