import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    url = url_entry.get()
    
    # Crea el código QR
    qr = qrcode.QRCode(version=1, box_size=5, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    
    # Genera la imagen del código QR
    qr_image = qr.make_image(fill="black", back_color="white")
    
    # Muestra la imagen del código QR en la ventana
    image = ImageTk.PhotoImage(qr_image)
    qr_label.configure(image=image)
    qr_label.image = image
    
    # Muestra un mensaje de éxito
    tk.messagebox.showinfo("Generación Exitosa", "El código QR ha sido generado exitosamente.")
    
# Crea la ventana principal
window = tk.Tk()
window.title("Generador de Código QR")
window.geometry("400x300")  # Ancho x Alto de la ventana

# Crea una etiqueta y un campo de entrada para la URL
url_label = tk.Label(window, text="URL:")
url_label.pack()

url_entry = tk.Entry(window)
url_entry.pack()

# Crea un botón para generar el código QR
generate_button = tk.Button(window, text="Generar", command=generate_qr_code)
generate_button.pack()

# Crea una etiqueta para mostrar el código QR generado
qr_label = tk.Label(window)
qr_label.pack()


window.mainloop()