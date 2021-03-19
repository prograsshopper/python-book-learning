'''
스레드
- os상에서 작동되는 스케줄링 가능한 인스트럭션의 순차적 흐름
- Program counter, stack, register 를 비롯한 식별자로 구성
- 공유 자원 사이에서 상호작용 가능, 스레드간 통신  및 메모리 공유도 가능

- 사용자 레벨 스레드, 커널 레벨 스레드 두 종류

컨텍스트 스위칭
- 짧은 시간동안 여러개의 스레드가 병렬로 작동한단 뜻

GIL(Global Interpreter Lock)의 한계
- 병렬 파이썬 코드를 실행할 때 여러 스레드의 사용을 제한하는 상호 배제 락
- 한번에 1개의 스레드만 유지하는 락이며 스레드를 자체 코드에서 실행하려면 자체 코드 실행전에 락을 먼저 점유해야만 가능
'''

# 예제: 동시에 그림 다운로드 하기
'''
main함수 내에서 빈 배열의 스레드를 생성하고, 스레드 배열에 추가하는 방식으로
새 스레드 객체를 생성하고, 스레드를 시작.
마지막으로 스레드 배열 i를 호출해 배열을 반복하며 각 스레드 내의 join 메소드를 호출.
'''
import threading
import urllib.request
import time

def download_image(image_path, file_name):
  print("Downloading Image from ", image_path)
  urllib.request.urlretrieve(image_path, file_name)
  print("Completed Download")

def execute_thread(i): 
  image_name = "temp/image-" + str(i) + ".jpg"
  download_image("http://lorempixel.com/400/200/sports", image_name)

def main():
  t0 = time.time()
  threads = []

  for i in range(10):
    thread = threading.Thread(target=execute_thread, args=(i,))
    threads.append(thread)
    thread.start()
  
  for i in threads:
    i.join()

  t1 = time.time()
  total_time = t1 - t0
  print("Total Execution Time {}".format(total_time))

if __name__ == '__main__':
    main()