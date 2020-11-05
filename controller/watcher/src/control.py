import time #スリープ関数用．必須じゃない．

import RPi.GPIO as GPIO #GPIO用のライブラリ


PIN = 18    # サーボモータの信号線を接続したGPIO番号の設定
GPIO.setmode(GPIO.BCM)    # ポート番号の指定方法をGPIO番号に指定
GPIO.setup(PIN, GPIO.OUT)    # GPIOを出力に設定
servo = GPIO.PWM(PIN, 50)    # PWMの周波数を50に設定
servo.start(3.0)   # PWMのデューティー比を2.5で開始


def servo_lock():
    # servo.start(2.5)   # PWMのデューティー比を2.5で開始
    servo.ChangeDutyCycle(3.0) #サーボを0°まで動かして，ロック
    print("locked! (degree is 0)")
    time.sleep(1) #サードの動作時間
    # servo.stop()    # サーボの制御を終了

def servo_unlock():
    # servo.start(4.08)   # PWMのデューティー比を2.5で開始
    servo.ChangeDutyCycle(6.9) #サーボを30°まで動かして，アンロック
    print("unlocked! (degree is 30)")
    time.sleep(1) #サードの動作時間
    # servo.stop()    # サーボの制御を終了

def main():
    while True:
        x = input("アンロック＝u,o || ロック=l,c || 終了-左記以外：") #キーボード入力

        if x == "u" or x == "o":
            servo_unlock() #サーボのアンロック用関数を呼び出し
        elif x == "l" or x == "c":
            servo_lock() #サーボのロック用関数を呼び出し
        else:
            break #このプログラムの終了

        time.sleep(1) #サードの動作時間

    servo.stop()    # サーボの制御を終了
    GPIO.cleanup()    # GPIOポートのクリア

if __name__ == '__main__':
    main()