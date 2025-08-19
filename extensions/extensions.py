file = input("File Name: ").lower().strip()


newf = file.split(".")


name = newf[-1]

match name:
    case "jpg":
        print(f"image/jpeg")
    case "gif":
        print(f"image/gif")
    case "jpeg":
        print(f"image/jpeg")
    case "png":
        print(f"image/png")
    case "pdf":
        print(f"application/pdf")
    case "txt":
        print(f"text/plain")
    case "zip":
        print(f"application/zip")
    case _:
        print(f"application/octet-stream")
