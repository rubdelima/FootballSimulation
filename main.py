from simulations import *

if __name__ == '__main__':
    arsenal = Time('Arsenal', defesa=81, ataque=83, meio=85)
    city = Time('City', defesa=85, ataque=88, meio=86)
    united = Time('United', defesa=79, ataque=80, meio=81)
    chelsea = Time('Chelsea', defesa=82, ataque=81, meio=79)
    liverpool = Time('Liverpool', defesa=83, ataque=85, meio=83)
    spurs = Time('Tottenhan1', defesa=79, ataque=84, meio=81)
    t10 = Time('t10', defesa=10, ataque=10, meio=10)
    t75 = Time('t75', defesa=75, ataque=75, meio=75)
    times = [arsenal, city, united, chelsea, liverpool, spurs, t10, t75]
    times2 =[]
    for i in range(4):
        times2.append(Time(f't{79+i}D', defesa=79+1+i, ataque=79+i, meio=79+i))
        times2.append(Time(f't{79+i}M', defesa=79+i, ataque=79+i, meio=79+1+i))
        times2.append(Time(f't{79+i}A', defesa=79+1+i, ataque=79+1+i, meio=79+i))
    times.extend(times2)
    
    simulate_league(times, 10000)