import tkinter as tk

# Global değişkenler
base = 0
side = 0
height = 0
apex_x = 0
apex_y = 0
base_half = 0
canvas_width = 800
canvas_height = 600
taxicab_text = None
triangle = None  # Üçgen çizimini saklamak için global değişken

def draw_triangle():
    global base, side, height, apex_x, apex_y, base_half, triangle
    
    base_input = base_entry.get()
    side_input = side_entry.get()
    height_input = height_entry.get()

    # Giriş alanlarının boş olup olmadığını kontrol et
    if not base_input or not side_input or not height_input:
        # Eğer herhangi bir giriş alanı boşsa, kullanıcıya uyarı ver
        messagebox.showwarning("Uyarı", "Lütfen tüm giriş alanlarını doldurun.")
        return

    base = float(base_input)
    side = float(side_input)
    height = float(height_input)

    apex_x = canvas_width / 2
    apex_y = canvas_height - height
    base_half = base / 2

    # Üçgeni çiz
    canvas.delete("all")  # Önceki çizimleri temizle
    triangle = canvas.create_polygon(
        apex_x, apex_y,
        apex_x - base_half, apex_y + height,
        apex_x + base_half, apex_y + height,
        fill="#ADD8E6",  # lightblue renginin alfa değeri azaltılmış hali
        outline="black"
    )

    # Kenar uzunluklarını ve yüksekliği yaz
    canvas.create_text(apex_x, apex_y + height + 10, text=f"{base}", fill="black", font=("Arial", 12, "bold"))
    canvas.create_text(apex_x - base_half - 30, apex_y + height / 2, text=f"{side}", fill="black", font=("Arial", 12, "bold"))
    canvas.create_text(apex_x + base_half + 30, apex_y + height / 2, text=f"{side}", fill="black", font=("Arial", 12, "bold"))
    canvas.create_text(apex_x, apex_y - 10, text=f"{height}", fill="black", font=("Arial", 12, "bold"))

def calculate_taxicab_diameter():
    global taxicab_text, triangle
    triangle = draw_triangle()  # Üçgeni çiz
    # Taxicab çapını hesapla
    taxicab_diameter = base + 2 * side
    # Eğer önceki taxicab çapı metni varsa, sil
    if taxicab_text:
        canvas.delete(taxicab_text)
    # Yeni taxicab çapını göster
    taxicab_text = canvas.create_text(apex_x, apex_y + height + 30, text=f"Taxicab Çapı: {taxicab_diameter}", fill="black", font=("Arial", 12, "bold"))
    # Üçgenin önüne getir
    canvas.tag_raise(triangle, taxicab_text)  # triangle ve taxicab_text yer değiştirdi

def drag_triangle(event):
    # Fare hareketi ile yüksekliği güncelle
    new_height = canvas_height - event.y
    height_entry.delete(0, tk.END)
    height_entry.insert(0, str(new_height))
    draw_triangle()

# Pencere oluştur
window = tk.Tk()
window.title("İkizkenar Üçgen Çizdirme")

# Canvas oluştur
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

# Kullanıcı giriş alanları
base_label = tk.Label(window, text="Taban Uzunluğu:")
base_label.pack()
base_entry = tk.Entry(window)
base_entry.pack()

side_label = tk.Label(window, text="Yan Kenar Uzunluğu:")
side_label.pack()
side_entry = tk.Entry(window)
side_entry.pack()

height_label = tk.Label(window, text="Yükseklik:")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

# Çizim butonu
draw_button = tk.Button(window, text="Çiz", command=draw_triangle)
draw_button.pack()

# Taxicab çapını hesapla ve göster butonu
calculate_taxicab_button = tk.Button(window, text="Taxicab Çapını Hesapla", command=calculate_taxicab_diameter)
calculate_taxicab_button.pack()

# Pencerenin boyutunu ayarla
window.geometry(f"{canvas_width + 50}x{canvas_height + 200}")

# Fare olaylarını bağla
canvas.bind("<B1-Motion>", drag_triangle)

# Pencereyi aç
window.mainloop()











