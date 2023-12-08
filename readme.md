

## CommandExecutor
    Запускает цикл
      делегирует запрос получения команды DialogWithUser
      обрабатывает полученную команду 
        если команда неизвестна - делегирует отображение пользователю сообщения об ошибке классу DialogWithUser 
        если команда "рассчитать статистику", делегирует получение статистики классу StatisticsCommands и делегирует отображение пользователю сообщения классу DialogWithUser
        если команда "узнать статус пациента" / "повысить статус пациента" / "понизить статус пациента" / "выписать пациента"
          делегирует выполнение команды соответстующему методу класса PatientCommands
        если команда "стоп" - прерывает цикл

    В конструкторе получает объекты классов DialogWithUser, StatisticsCommands и PatientCommands

## PatientCommands

    Класс обработки статуса пациента по id 
    
    обрабатывает ошибки PatientIdNotIntegerOrNotPositive/ PatientIdNotExist
        и делегирует отображение пользователю сообщения об ошибке классу DialogWithUser 
    Повышает статус пациента
          - делигирует проверку возможность повышения статуса пациента PatientsDB
                если да, делегирует повышение статуса пациента PatientsDB
                    делегирует отображение пользователю сообщения о новом статусе классу DialogWithUser
                если нет,
                    делегирует запрос выписки пациента DialogWithUser
                      если True
                          делегирует выписку пациента классу PatientsDB
                          формирует сообщение о выписке пациента 
                          делегирует отображение пользователю сообщения классу DialogWithUser 
                      если False
                          формирует сообщение о сохранении текущего статуса пациента
                          делегирует отображение пользователю сообщения классу DialogWithUser 
    Понижает статус пациента
        делегирует проверку возможности понижения статуса классу PatientsDB
            если False
              делегирует уведомление пользователя о невозможности изменения статуса пациента классу DialogWithUser
            если True
              делегирует понижение статуса классу PatientsDB
              формирует сообщение о изменении статуса пациента
              делегирует отображение пользователю сообщения классу DialogWithUser 
    Запрашивает текущий статус пациента через PatientsDB
        формирует сообщение о изменении статуса пациента
        делегирует отображение пользователю сообщения классу DialogWithUser 
    Выписавает пациента 
        делегирует выписку пациента классу PatientsDB
        формирует сообщение о выписке пациента 
        делегирует отображение пользователю сообщения классу DialogWithUser 

    В конструкторе получает объекты классов DialogWithUser и PatientsDB
    взаимодействует с PatientIdNotIntegerOrNotPositive, PatientIdNotExist

## PatientDB
    Класс базы данных пациентов

    высчитывает index пациента на основе полученного id 
        проверят что пациент с таким index существует в бд  и выдаёт ошибку PatientIdNotExist если нет 
    возвращает статус пациента по id 
    проверяет возможно ли повысить статус пациента по id, если да возвращает True, если нет False
    повышает статус пациента по id 
    проверяет возможно ли понизить статус пациента по id, если да возвращает True, если нет False
    понижает статус пациента по id 
    выписывает пациента по id (удалаяет запись пациента из бд)
    возвращает статистику базы пациентов(общее кол-во пациентов, кол-во пациентов по каждому сузествующему в бд статусу)
    
    Содержит базу пациентов
    получает базу в конструкторе 
    если база не передана, сам пустую создает 

    С кем взаимодействует:
      PatientIdNotExist
        

## StatisticsCommands
 
    делегирует расчет статистики классу PatientsDB
    формирует сообщение с расчитанной статистикой пациентов 
    возвращает сообщение со статистикой 

    В конструкторе получает объект класса PatientsDB


## PatientIdNotIntegerOrNotPositive / PatientIdNotExist
    Классы ошибок id пациента 
  
    PatientIdNotIntegerOrNotPositive  если id пациента не число, отрицательное или 0
    PatientIdNotExist  если id пациента не найдено в бд 

## DialogWithUser
    Класс взаимодействия с пользователем 
    
    - Выводит пользователю сообщение с запросом получения новых данных и возвращает введенные пользователем данные 
    - Выводит пользователю обработанных данных
    - Запрашивает у рользователя id пациента, возврщает id пациента 
        преобразует введенную строку в число 
        если id пациента меньше 0/ не число выкидывает ошибку PatientIdNotIntegerOrNotPositive
    - Запрашивает у пользователя подтверждение выписки пациента 
        если да возвращает True
        если нет(любая команда, кроме да) возвращает False

    Взаимодействует с PatientIdNotIntegerOrNotPositive