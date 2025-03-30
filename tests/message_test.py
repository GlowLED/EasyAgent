from easyagent.messages import TextMessage, ImageMessage

text_message = TextMessage("Hello, world!", source="user")
print(text_message)

msg1 = TextMessage("Hello, ", source="user")
msg2 = TextMessage("world!", source="user")
combined_msg = msg1 + msg2
print(combined_msg)
print(len(combined_msg))
print(combined_msg.source)
print(combined_msg[0: 5])

img = ImageMessage("tests/test.jpg", source="user")
print(img)
img.show()