resource "kubernetes_namespace" "abelovn_dev" {
  metadata {
    annotations = {
      name = "This namespace is for development"
    }

    labels = {
      mylabel = "dev"
    }

    name = "development"
  }
}

resource "kubernetes_namespace" "abelovn_prod" {
  metadata {
    annotations = {
      name = "This namespace is for productive env"
    }

    labels = {
      mylabel = "prod"
    }

    name = "production"
  }
}

resource "kubernetes_namespace" "abelovn_cicd" {
  metadata {
    annotations = {
      name = "This namespace is for cicd"
    }

    labels = {
      mylabel = "cicd"
    }

    name = "cicd"
  }
}


resource "kubernetes_namespace" "abelovn_monitoring" {
  metadata {
    annotations = {
      name = "This namespace is for monitoring"
    }

    labels = {
      mylabel = "monitoring"
    }

    name = "monitoring"
  }
}



