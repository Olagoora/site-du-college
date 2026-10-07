# ============================================================
# COMPILATION AUTOMATIQUE SCSS -> CSS
# APPLICATION + FORM
# ============================================================


# ============================================================
# CONFIGURATION
# ============================================================

$ScssRoots = @(
    @{
        Name = "APPLICATION"
        Scss = "app\application\static\application\scss"
        Css  = "app\application\static\application\css"
    },
    @{
        Name = "FORM"
        Scss = "app\form\static\form\scss"
        Css  = "app\form\static\form\css"
    }
)


# ============================================================
# FONCTION DE COMPILATION
# ============================================================

function Compile-ScssTree {

    param (
        [string]$Name,
        [string]$ScssRoot,
        [string]$CssRoot
    )


    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "        $Name : SCSS -> CSS" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""


    # --------------------------------------------------------
    # Vérification du dossier SCSS
    # --------------------------------------------------------

    if (-not (Test-Path $ScssRoot)) {

        Write-Host "ERREUR : dossier SCSS introuvable :" -ForegroundColor Red
        Write-Host $ScssRoot -ForegroundColor Red
        Write-Host ""

        return
    }


    # --------------------------------------------------------
    # Création du dossier CSS
    # --------------------------------------------------------

    if (-not (Test-Path $CssRoot)) {

        New-Item `
            -ItemType Directory `
            -Path $CssRoot `
            -Force |
            Out-Null
    }


    # --------------------------------------------------------
    # Recherche de TOUS les fichiers .scss
    # --------------------------------------------------------

    $ScssFiles = Get-ChildItem `
        -Path $ScssRoot `
        -Filter "*.scss" `
        -Recurse `
        -File


    if ($ScssFiles.Count -eq 0) {

        Write-Host "Aucun fichier SCSS trouvé." -ForegroundColor Yellow
        return
    }


    # --------------------------------------------------------
    # Compilation de chaque fichier
    # --------------------------------------------------------

    foreach ($File in $ScssFiles) {

        $ScssFile = $File.FullName


        # ----------------------------------------------------
        # Chemin relatif depuis le dossier SCSS
        # ----------------------------------------------------

        $RelativePath = $ScssFile.Substring(
            (Resolve-Path $ScssRoot).Path.Length
        ).TrimStart("\", "/")


        # ----------------------------------------------------
        # SCSS -> CSS
        # ----------------------------------------------------

        $CssRelativePath = [System.IO.Path]::ChangeExtension(
            $RelativePath,
            ".css"
        )


        # ----------------------------------------------------
        # Chemin CSS final
        # ----------------------------------------------------

        $CssFile = Join-Path `
            $CssRoot `
            $CssRelativePath


        # ----------------------------------------------------
        # Création automatique du sous-dossier CSS
        # ----------------------------------------------------

        $CssDirectory = Split-Path `
            $CssFile `
            -Parent


        if (-not (Test-Path $CssDirectory)) {

            New-Item `
                -ItemType Directory `
                -Path $CssDirectory `
                -Force |
                Out-Null
        }


        # ----------------------------------------------------
        # Affichage
        # ----------------------------------------------------

        Write-Host "SCSS :" -NoNewline -ForegroundColor DarkGray
        Write-Host " $RelativePath"

        Write-Host "  -> CSS :" -NoNewline -ForegroundColor DarkGray
        Write-Host " $CssRelativePath" -ForegroundColor Green


        # ----------------------------------------------------
        # Compilation
        # ----------------------------------------------------

        npx sass $ScssFile $CssFile


        # ----------------------------------------------------
        # Vérification
        # ----------------------------------------------------

        if ($LASTEXITCODE -ne 0) {

            Write-Host ""
            Write-Host "ERREUR pendant la compilation :" -ForegroundColor Red
            Write-Host $ScssFile -ForegroundColor Red
            Write-Host ""

        }
    }


    Write-Host ""
    Write-Host "Compilation $Name terminée." -ForegroundColor Green
}


# ============================================================
# COMPILATION DE TOUS LES PROJETS
# ============================================================

foreach ($Root in $ScssRoots) {

    Compile-ScssTree `
        -Name $Root.Name `
        -ScssRoot $Root.Scss `
        -CssRoot $Root.Css
}


# ============================================================
# FIN
# ============================================================

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "       COMPILATION TERMINEE" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""