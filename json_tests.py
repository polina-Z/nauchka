import unittest
from ser_create import my_dump
from ser_create import my_load
from ser_create.json_serializer import JsonSerializer
import types

js = JsonSerializer()

class TestingObjects(unittest.TestCase):
    
    def tearDown(self):
        dumper = js.dumps(self.tested_obj)
        self.loader = js.loads(dumper)
        self.assertTrue(self.loader == self.tested_obj)
        
    def test_none(self):
        self.tested_obj = None
        
    def test_bool_True(self):
        self.tested_obj = True
    
    def test_bool_False(self):
        self.tested_obj = False
    
    def test_int(self):
        self.tested_obj = 323464
    
    def test_float(self):
        self.tested_obj = 3.14159265359
        
    def test_complex(self):
        self.tested_obj = complex(1, 2)
        
    def test_str(self):
        self.tested_obj = "Hello from test"
    
    def test_list(self):
        self.tested_obj = [1, 2, 3, 4, 5]
    
    def test_tuple(self):
        self.tested_obj = (1, 2, 3, 4, 5)
    
    def test_range(self):
        self.tested_obj = range(1, 5, 1)
    
    def test_bytes(self):
        self.tested_obj = bytes.fromhex("d0 9f d1 80 d0 b8 d0 b2 d0 b5 d1 82")
        
    def test_bytearray(self):
        self.tested_obj = bytes.fromhex("d0 a2 d0 b5 d1 81 d1 82 d0 b8 d0 bc")
    
    def test_memoryview(self):
        self.tested_obj = memoryview(bytes.fromhex("d0 9b d0 b0 d0 b1 d1 83"))
    
    def test_set(self):
        self.tested_obj = {1, 2, 3, 4, 5}
        
    def test_frozenset(self):
        self.tested_obj = frozenset({1, 2, 3, 4, 5})
        
    def test_dict(self):
        self.tested_obj = {"a": 1, "b": 2, "c": 3}
   
    def test_mappingproxytype(self):
        self.tested_obj = types.MappingProxyType({"a": 1, "b": 2, "c": 3})
  
        
    
if __name__ == "__main__":
    unittest.main()
