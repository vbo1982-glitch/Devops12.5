resource "helm_release" "argocd" {
  name             = "argocd"
  repository       = "https://argoproj.github.io/argo-helm"
  chart            = "argo-cd"
  namespace        = "argocd"
  create_namespace = true
  timeout          = 600 # Додали збільшений таймаут

  depends_on = [
    helm_release.nginx_ingress
  ]

  values = [
    <<-EOT
    server:
      extraArgs:
        - --insecure
      ingress:
        enabled: true
        ingressClassName: nginx
        hosts:
          - argocd.vitaliy.devops13.test-danit.com
    EOT
  ]
}