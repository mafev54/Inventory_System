from models.supplies import Supplies as SuppliesModel

class SuppliesService():
    def __init__(self, db):
        self.db = db

    def get_supplie(self):
        result = self.db.query(SuppliesModel).all()
        return result
    
    def create_supplie(self, supplie: SuppliesModel):
        new_supplie = SuppliesModel(
            purchase_price=supplie.purchase_price
        )
        self.db.add(new_supplie)
        self.db.commit()
        self.db.refresh
        return
    
    
    def get_for_id(self, id:int):
        result = self.db.query(SuppliesModel).filter(SuppliesModel.id == id).first()
        return result
    
    def update_supplie(self,data):
        supplie = self.db.query(SuppliesModel).filter(SuppliesModel.id == data.id).first()
        supplie.purchase_price = data.purchase_price
        return
    