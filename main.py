def on_a_pressed():
    mySprite.start_effect(effects.confetti, randint(100, 600))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

mySprite: Sprite = None
scene.set_background_color(6)
game.splash("My monkey better than yours")
mySprite = sprites.create(img("""
        . . . . f f f f f . . . . . . . 
            . . . f e e e e e f . . . . . . 
            . . f d d d d e e e f f . . . . 
            . c d d d d d d e e d d f . . . 
            . c d f d d f d e e b d c . . . 
            c d d f d d f d e e b d c . f f 
            c d e e d d d d e e f c . f e f 
            c d f f d c d e e e f . . f e f 
            . f c c c d e e e f f . . f e f 
            . . f f f f f e f e e f . f e f 
            . . . . f e f e f e f e f f f . 
            . . f f e f e e f f e e e f . . 
            . f e f f e e f f f e e e f . . 
            f d d b d d c f f f f f f b f . 
            f d d c d d d f . . f c d d f . 
            . f f f f f f f . . . f f f . .
    """),
    SpriteKind.player)