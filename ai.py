from opengpt.forefront.model import Model
from opengpt.forefront.tools.system.email_creation import Email

client = ""
sessionID = ""

forefront = Model(sessionID=sessionID, client=client, model="gpt-4")

while True:
    prompt = input("Enter Query: ")

    forefront.SetupConversation(prompt)

    for r in forefront.SendConversation():
        print(r.choices[0].delta.content, end='')
    print()
