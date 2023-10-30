controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.startEffect(effects.confetti, randint(100, 600))
})
let mySprite: Sprite = null
scene.setBackgroundColor(6)
game.splash("My monkey better than yours")
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
