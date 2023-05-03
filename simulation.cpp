#include<bits/stdc++.h>
using namespace std;

vector<string> zonas = {"gol2", "def1", "meio1", "meio", "meio2", "def2", "gol1"};

int randomRange(int n){
    return rand() % (n + 1);
}

class Time{
    public:
    string nome;
    int defesa, ataque, meio, overall, titulos_liga, titulos_copa, pontos_totais;
    int vitorias, derrotas, empates, gols_pro, gols_contra;

    Time(string nome, int defesa, int ataque, int meio) {
        this->nome = nome;
        this->defesa = defesa;
        this->ataque = ataque;
        this->meio = meio;
        this->overall = (defesa + ataque + meio) / 3;
        this->titulos_liga = 0;
        this->titulos_copa = 0;
        this->pontos_totais = 0;
        this->vitorias = 0;
        this->derrotas = 0;
        this->empates = 0;
        this->gols_pro = 0;
        this->gols_contra = 0;
    }
    /*
    friend ostream& operator<<(ostream& os, const Time& mc) {
        os << mc.nome;
        return os;
    }
    */

    int get_pontos(){
        unsigned int valor = (vitorias*3) + empates;
        return valor;
    }

    string get_stats() {
        int jogos = vitorias + derrotas + empates;
        int sg = gols_pro - gols_contra;
        stringstream ss;
        ss << left << setw(15) << nome << right << setw(2) << jogos << "  " << setw(2) << vitorias << "  " << setw(2) << empates << "  " << setw(2) << derrotas << "  " << setw(3) << gols_pro << "  " << setw(3) << gols_contra << "  " << setw(4) << sg << "  " << setw(2) << get_pontos();
        return ss.str();
    }

    void clear(){
        this->pontos_totais = pontos_totais + get_pontos();
        this->vitorias = 0;
        this->derrotas = 0;
        this->empates = 0;
        this->gols_pro = 0;
        this->gols_contra = 0;
    }

};

int vantagem(int t1, int t2) {
    int t3 = t1 + (t1-t2)*5;
    if (t3<0)
        t3 = t1;
    return t3;
}

int alg2(Time t1, Time t2, int zone){
    int z1,z2;
    switch (zone){
    case 1: z1 = t1.defesa ; z2 = t2.ataque; break;
    case 2: z1 = (t1.meio + t1.defesa)/2; z2 = (t2.meio + t2.ataque)/2; break;
    case 3: z1 = t1.meio; z2 = t2.meio;break;
    case 4: z1 = (t1.meio + t1.ataque)/2; z2 =(t2.meio + t2.defesa)/2; break;
    case 5: z1 = t1.ataque ; z2=t2.defesa; break;
    default:break;
    }
    int meio = 2*(z1+z2) - (abs(z1-z2)*10);
    if (meio < 0){meio =0;}
    z1 =  vantagem(z1,z2);
    z2 =  vantagem(z2,z1);
    int a = randomRange(z1+z2+meio);
    if (a < z1){return 1;}
    else if (a < z1+z2) {return -1;}
    else {return 0;}
}

pair <int, int> simulation(Time time1, Time time2){
    int time1_p = 0;
    int time2_p = 0;
    int zone = 3;
    for (int i = 0; i <90; i++){
        zone = zone + alg2(time1,time2, zone);
        if (zonas[zone] == "gol1"){
            time1_p++;zone = 3;
        }else if (zonas[zone] == "gol2"){
            time2_p++;zone = 3;
        }
    }
    return make_pair(time1_p,time2_p);
}


vector<pair<Time, Time>> get_rounds(vector<Time>& lista) {
    vector<pair<Time, Time>> a;
    int jogos = 0;
    for (unsigned int i = 0; i < lista.size(); i++){
        for (unsigned int j = 0; j < lista.size(); j++){
            if (i != j){
                a.push_back(make_pair(lista[i], lista[j]));
            }
        }
    }
    return a;
}

void simulate_league(vector<Time>& lista, int rounds = 1) {
    for (int r = 0; r < rounds; r++) {
        auto liga = get_rounds(lista);
        for (auto& j : liga) {
            pair<int, int> b = simulation(j.first, j.second);
            if (b.first > b.second) {
                j.first.vitorias++;
                j.second.derrotas++;
            } else if (b.second > b.first) {
                j.second.vitorias++;
                j.first.derrotas++;
            } else {
                j.first.empates++;
                j.second.empates++;
            }
            j.first.gols_pro += b.first;
            j.first.gols_contra += b.second;
            j.second.gols_pro += b.second;
            j.second.gols_contra += b.first;
        }
        sort(lista.begin(), lista.end(), [](Time& t1, Time& t2) {
            if (t1.get_pontos() != t2.get_pontos()) {
                return t1.get_pontos() > t2.get_pontos();
            } else {
                return t1.gols_pro - t1.gols_contra > t2.gols_pro - t2.gols_contra;
            }
        });
        for (auto& k : lista) {
            k.clear();
        }
        lista[0].titulos_liga++;
    }
    sort(lista.begin(), lista.end(), [](Time& t1, Time& t2) {
        if (t1.titulos_liga != t2.titulos_liga) {
            return t1.titulos_liga > t2.titulos_liga;
        } else {
            return t1.pontos_totais > t2.pontos_totais;
        }
    });
    for (auto& i : lista) {
        cout << left << setw(15) << i.nome << setw(5) << i.titulos_liga << setw(8) << i.pontos_totais << endl;
    }
}

int main(){
    Time arsenal("Arsenal", 81, 83, 85);
    Time city("City", 85, 88, 86);
    Time united("United", 79, 80, 81);
    Time chelsea("Chelsea", 82, 81, 79);
    Time liverpool("Liverpool", 83, 85, 83);
    Time spurs("Tottenhan1", 79, 84, 81);
    Time t10("t10", 10, 10, 10);
    Time t75("t75", 75, 75, 75);
    vector<Time> times = {arsenal, city, united, chelsea, liverpool, spurs, t10, t75};
    vector<Time> times2;
    
    for (int i = 0; i < 4; i++) {
    times2.push_back(Time("t" + to_string(79+i) + "D", 79+1+i, 79+i, 79+i));
    times2.push_back(Time("t" + to_string(79+i) + "M", 79+i, 79+i, 79+1+i));
    times2.push_back(Time("t" + to_string(79+i) + "A", 79+1+i, 79+1+i, 79+i));
    }
    times.insert(times.end(), times2.begin(), times2.end());
    
    simulate_league(times, 10000);

}