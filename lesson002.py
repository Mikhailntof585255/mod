def send_email (message,recipient,sender='university.help@gmil.com'):
   sender_1='university.help@gmil.com'
   if sender==recipient:
      print("Нельзя отправить письмо самому себе")
      breakpoint()
   x_1 = 0
   for i in range(len(sender)):
       if sender[i] == '@':
          x_1 = 1
       if sender[i] ==range(len(sender)):
          if x_1 == 0:
            print("Невозможно отправить письмо с адреса ", sender, " на адрес ", recipient)

   x_1 = 0
   for i in range(len(recipient)):
       if recipient[i] == '@':
          x_1 = 1
       if recipient[i] == len(recipient):
          if x_1 == 0:
             print("Невозможно отправить письмо с адреса ", sender, " на адрес ", recipient)
             break
   A = []
   B = []
   C = []
   D = []
   A = list(sender);
   B = list(sender);
   C = list(recipient);
   D = list(recipient)
   A = sender[-4:len(sender)]
   C = recipient[-4:len(recipient)]
   B = sender[-3:len(sender)]
   D = recipient[-3:len(recipient)]
   if (A == '.com' or A == '.net' or B == '.ru') and (C == '.com' or C == '.net' or D == '.ru'):
        if sender_1==sender:
               print("Письмо успешно отправлено c адреса ",sender," на адрес",recipient)
               print(message)
        elif sender_1 != sender:
               print("НЕСТАНДАПТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, ' на адрес', recipient)
               print(message)
   else:
        print("Невозможно отправить письмо с адреса ", sender, " на адрес ", recipient)



#send_email('это сообщение для проверки связи',"vasyok1337@gmail.com")
#Письмо успешно отправлено c адреса  university.help@gmil.com  на адрес vasyok1337@gmail.com
#это сообщение для проверки связи

#send_email('Вы видите это сообщение как лучший студент курса!',"urdan.fan@mail.ru","uban.teache@mail.ru")
#НЕСТАНДАПТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса  uban.teache@mail.ru  на адрес urdan.fan@mail.ru
#Вы видите это сообщение как лучший студент курса!

#send_email('Пожалуйта, исправьте задание','urban.student@mail.ru','urban.teache@mail.uk')
#Невозможно отправить письмо с адреса  uban.teache@mail.uk  на адрес  urban.student@mail.ru
send_email('напоминаю самому себе о вurban.student@mail.ruебинаре','urban.student@mail.ru')
#Нельзя отправить письмо самому себе
#> c:\pythonprogectsurban\pythonproject\lesson002.py(6)send_email()
#-> x_1 = 0
#(Pdb)