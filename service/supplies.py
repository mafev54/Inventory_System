from models.supplies import Supplies as SuppliesModel

class SuppliesService():
    def __init__(self, db):
        self.db = db

    def get_supplie(self):
        result = self.db.query(SuppliesModel).all()
        return result
    
    def create_supplie(self, supplie: SuppliesModel):
        new_supplie = SuppliesModel(
            purchase_price=supplie.purchase_price,
            supplier_id = supplie.supplier_id,
            product_id = supplie.product_id
        )
        self.db.add(new_supplie)
        self.db.commit()
        self.db.refresh
        return
    
    
    def get_for_id(self, id:int):
        result = self.db.query(SuppliesModel).filter(SuppliesModel.id == id).first()
        return result
    
    def update_supplie(self, id : int, data):
        supplie = self.db.query(SuppliesModel).filter(SuppliesModel.id == id).first()
        supplie.supplier_id = data.supplier_id
        supplie.purchase_price = data.purchase_price
        supplie.product_id = data.product_id
        
        return
    
    def delete_supplie(self,id:int):
        self.db.query(SuppliesModel).filter(SuppliesModel.id == id).delete()
        self.db.commit()
        return
    