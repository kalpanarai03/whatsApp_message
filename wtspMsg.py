import pywhatkit as pwk

def send_whatsapp_message(phone_number, message, hour, minute):
    try:
        pwk.sendwhatmsg(f"+{phone_number}", message, hour, minute)
        print("WhatsApp message sent successfully!")
    except Exception as e:
        print(f"Failed to send WhatsApp message: {e}")


recipient_phone_number = "+91-9915084299" 
message_content = "Hello, this is a test message from Python by Kalpana Rai!"  
sending_hour = 22 
sending_minute = 4

send_whatsapp_message(recipient_phone_number, message_content, sending_hour, sending_minute)

