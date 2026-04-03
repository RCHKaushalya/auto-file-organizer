from organizer import organize_files

if __name__ == "__main__":
    # Default to Downloads folder
    from pathlib import Path
    downloads_path = str(Path.home() / "Downloads")
    summary, unsorted = organize_files(downloads_path)

    print("\nSummary Report:")
    for folder, count in summary.items():
        print(f"{folder}: {count} files")
    if unsorted:
        print("\nUnsorted files:\n")
        for file in unsorted:
            print(f"- {file}")
