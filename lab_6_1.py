
"""
Известны данные о мощности двигателя (в лошадиных силах – л. с.) и стоимости 30 марок
легковых автомобилей. Напечатать стоимость каждого из автомобилей, у которых мощность
двигателя не превышает 80 л. с.
"""
import random

if __name__ == "__main__":
        auto =  [["Smart fortwo", 71, random.randint(800000, 1800000)],
                ["Chevrolet Niva", 80, random.randint(800000, 1800000)],
                ["Datsun on-DO", 82, random.randint(800000, 1800000)],
                ["Renault Logan", 82, random.randint(800000, 1800000)],
                ["Lada 4x4 Urban", 83, random.randint(800000, 1800000)],
                ["Ford Focus (Ambiente)", 85, random.randint(800000, 1800000)],
                ["Ravon R2", 85, random.randint(800000, 1800000)],
                ["Datsun mi-DO", 87, random.randint(800000, 1800000)],
                ["Lada Granta", 87, random.randint(800000, 1800000)],
                ["Lada Kalina", 87, random.randint(800000, 1800000)],
                ["Lada Priora", 87, random.randint(800000, 1800000)],
                ["Lada Largus", 87, random.randint(800000, 1800000)],
                ["Lifan Smily", 88, random.randint(800000, 1800000)],
                ["Skoda Rapid", 90, random.randint(800000, 1800000)],
                ["Volkswagen Polo", 90, random.randint(800000, 1800000)],
                ["Volkswagen Jetta", 90, random.randint(800000, 1800000)],
                ["Toyota Corolla", 99, random.randint(800000, 1800000)],
                ["FIAT 500", 100, random.randint(800000, 1800000)],
                ["Hyundai Solaris", 100, random.randint(800000, 1800000)],
                ["Hyundai i30", 100, random.randint(800000, 1800000)],
                ["KIA Rio, 100", random.randint(800000, 1800000)],
                ["FAW Oley, 102", random.randint(800000, 1800000)],
                ["Nissan Almera", 102, random.randint(800000, 1800000)],
                ["Lifan X50", 103, random.randint(800000, 1800000)],
                ["Brilliance H230 седан", 105, random.randint(800000, 1800000)],
                ["Geely Emgrand", 105, random.randint(800000, 1800000)],
                ["Chery Tiggo 2", 106, random.randint(800000, 1800000)],
                ["Lada XRAY (Optima)", 106, random.randint(800000, 1800000)],
                ["Lada Vesta", 106, random.randint(800000, 1800000)],
                ["Ravon R4", 106, random.randint(800000, 1800000)],
                ["Ravon Nexia", 107, random.randint(800000, 1800000)]]

        for i in range(len(auto)):
                if auto[i][1] <= 80:
                        print(auto[i])