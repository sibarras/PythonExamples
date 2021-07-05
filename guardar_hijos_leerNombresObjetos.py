from datetime import datetime, timedelta


class Medicine:
    declarations:dict[str, object] = globals()
    medicine_objects:list[object] = []

    def __init__(self, freq:timedelta, quantity:int=1, med_type:str='pill',\
                 last_dosis:datetime=datetime.now()) -> None:
        self.freq = freq
        self.quantity = quantity
        self.med_type = med_type
        self.last_dosis = last_dosis

        assert self.quantity > 0
        valid_types:list[str] = ['pill', 'syrup']
        if self.med_type not in valid_types:
            raise Exception("[ERROR]: Medicine Type is not valid.")

        self.with_dosis:bool = True
        self.next_dosis:datetime = self.last_dosis + self.freq
        self.__class__.medicine_objects.append(self)

    @property
    def name(self) -> str:
        glob = self.__class__.declarations
        return [name for name in glob if glob[name] is self][0]

    def change_next_dosis_date(self) -> None:
        self.last_dosis = datetime.now()
        self.next_dosis = self.last_dosis + self.freq

        if self.med_type == 'pill':
            self.quantity -= 1

        if self.quantity == 0:
            print("Se te acabo la medicina. Pide rapido antes de {}".format(self.next_dosis))
        elif self.quantity == -1:
            self.quantity = 0
            self.with_dosis = False
            print("Necesitas tomar ya y no tienes nada que tomar.")
    
    def __repr__(self) -> str:
        return "(Name:{}, Type:{}, Quantity:{}, Frequency:{})"\
                .format(self.name, self.med_type, self.quantity, self.freq)


if __name__ == "__main__":
    ibuprofeno = Medicine(freq=timedelta(hours=8), quantity=6)
    inmuneComplex = Medicine(freq=timedelta(days=1), quantity=12)
    
