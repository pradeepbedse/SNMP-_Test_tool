import tkinter as tk
import smtplib
from tkinter import messagebox

def send_email():
    # Get the user inputs from the entry fields
    sender_email = sender_entry.get()
    password = password_entry.get()
    recipient_email = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end")
    smtpserver= smtpserver_entry.get()
    smtp_port = smtpserver_port.get()
    print(smtp_port, smtpserver)
    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP(smtpserver,smtp_port)
        print(f"{smtpserver},{smtp_port}")
        server.starttls()
        # Login to the sender's email account
        server.login(sender_email, password)
        
        # Create the email message
        email_message = f"Subject: {subject}\n\n{message}"
        
        # Send the email
        server.sendmail(sender_email, recipient_email, email_message)
        server.quit()
        
        messagebox.showinfo("Email Sent", "Email sent successfully!")
    except smtplib.SMTPException as e:
        messagebox.showerror("Email Error", f"An error occurred while sending the email:\n\n{str(e)}")

# Create the main window
window = tk.Tk()
window.title("Email Sender")

# Create the labels
sender_label = tk.Label(window, text="Sender's Email:")
sender_label.pack()
sender_entry = tk.Entry(window)
sender_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

smtpserver_label = tk.Label(window, text="SMTPServer & Port")
smtpserver_label.pack()
smtpserver_entry = tk.Entry(window)
smtpserver_entry.pack()
smtpserver_port = tk.Entry(window)
smtpserver_port.pack()

recipient_label = tk.Label(window, text="Recipient's Email:")
recipient_label.pack()
recipient_entry = tk.Entry(window)
recipient_entry.pack()

subject_label = tk.Label(window, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(window)
subject_entry.pack()

message_label = tk.Label(window, text="Message:")
message_label.pack()
message_text = tk.Text(window, height=10, width=30)
message_text.pack()

send_button = tk.Button(window, text="Send Email", command=send_email)
send_button.pack()

# Start the Tkinter event loop
window.mainloop()
