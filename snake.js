class Snake {
    constructor() {
        this.spawn();
    }

    // added this
    spawn() {
        this.body = [];
        this.body.push({x: width/2, y: height/2});
        this.dir = 1;
        this.lastX = width/2;
        this.lastY = height/2;
    }

    draw() {
        fill(0);
        for (let b of this.body) {
            rect(b.x, b.y, width / GRID_SIZE, height / GRID_SIZE)
        }
    }

    update() {
        this.hitDetection();

        this.lastX = this.body[this.body.length-1].x;
        this.lastY = this.body[this.body.length-1].y;
        for (let i = this.body.length-1; i >= 1; i--) {
            this.body[i].x = this.body[i-1].x;
            this.body[i].y = this.body[i-1].y;
        }

        if (this.dir == 1) {
            this.body[0].x += width / GRID_SIZE;
        } else if (this.dir == 2) {
            this.body[0].y += height / GRID_SIZE;
        } else if (this.dir == 3) {
            this.body[0].x -= width / GRID_SIZE;
        } else if (this.dir == 4) {
            this.body[0].y -= height / GRID_SIZE;
        }
    }

    // added this
    hitDetection() {
        for (let i = 1; i < this.body.length; i++) {
            if (this.body[0].x == this.body[i].x && this.body[0].y == this.body[i].y) {
                this.spawn();
            }
        }
    }

    grow() {
        this.body.push({x: this.lastX, y: this.lastY});
    }

    hasEatenFood() {
        if (this.body[0].x == food.x && this.body[0].y == food.y) {
            return true;
        }
    }

}