locals {
  name = var.environment == "production" ? "dnd-character-creator" : "dnd-character-creator-${var.environment}"
}
