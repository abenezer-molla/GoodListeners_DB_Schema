Tables

Listener's Columns

  - listner_id (int) - PRIMARY KEY
  - listner_firstName (string)
  - listner_lastName (string)
  - listner_email (string)
  - listner_phoneNumber (big_int)

Talker's Columns -- the person that shares

  - talker_id(int) - PRIMARY KEY
  - listner_id(string) - ForeignKey('Doctors.doctor_id')
  - talker_firstName(string)
  - talker_lastName(string)
  - talker_email(string)
  - talker_phoneNumber(big_int)
