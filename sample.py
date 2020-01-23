from dumpKNP import KNP
import time

def main():

    knp = KNP()
    string = "今日は良い天気ですね"

    start = time.time()
    knp_result = knp.parse(string)
    for mrph in knp_result.mrph_list():
        print("原型:" + mrph.genkei + " 品詞:"+ mrph.hinsi)
    
    elapsed_time = time.time() - start
    print("-----------------")
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print("-----------------")
    knp.save()

if __name__ == '__main__':
    main()