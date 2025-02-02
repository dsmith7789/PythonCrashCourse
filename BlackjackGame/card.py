from typing import Optional
import pygame

from definitions import Definitions

class Card:
    def __init__(self, suit: str, face_value: str, card_back: Optional[bool]=False) -> None:
        self.definitions = Definitions()
        self.card_back = card_back
        self.suit = suit
        self.face_value = face_value 
        self.value = self.get_value(face_value)
        
    def __repr__(self) -> str:
        return f"{self.face_value} of {self.suit}"
    
    def get_value(self, face_value: str) -> int:
        if self.card_back:
            return 0
        if face_value in ["ace", "jack", "queen", "king"]:
            return 10
        else:
            return int(face_value)
    
    def fetch_image(self) -> pygame.surface.Surface:
        if self.card_back:
            image = pygame.image.load(f'images/cards/card_back.png')
        else:
            image = pygame.image.load(f'images/cards/{self.face_value}_of_{self.suit}.png')
        image = pygame.transform.scale(image, self.definitions.card_size)
        return image
