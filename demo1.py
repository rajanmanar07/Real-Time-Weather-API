from plyer import notification
def notifyme(title,message):
    notification.notify(title=title,
                              message=message,
                              app_icon=None,
                              timeout=3)

if __name__ == '__main__':
    notifyme('rajan','corona virus is spreading rapidly')

