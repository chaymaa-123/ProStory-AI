'use client'

import { Navigation } from '@/components/Navigation'
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { useState } from 'react'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import { Building2, Users } from 'lucide-react'

export default function AuthPage() {
  const [isSignUp, setIsSignUp] = useState(false)
  const [isCompany, setIsCompany] = useState(false)
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
    name: '',
  })
  const [isLoading, setIsLoading] = useState(false)
  const router = useRouter()

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    })
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)

    // Simulate API call
    await new Promise((resolve) => setTimeout(resolve, 500))

    // Navigate based on account type
    if (isSignUp && isCompany) {
      router.push('/dashboard')
    } else {
      router.push('/feed')
    }
  }

  return (
    <main className="min-h-screen flex flex-col bg-background">
      <Navigation currentPath="/auth" />

      <div className="flex-1 flex items-center justify-center px-4 py-12">
        <div className="w-full max-w-md">
          <Card className="p-8">
            {/* Header */}
            <div className="text-center mb-8">
              <h1 className="text-2xl font-bold text-foreground mb-4">
                {isSignUp ? 'Créer un compte' : 'Se connecter'}
              </h1>
              <p className="text-sm text-muted-foreground mb-4">
                {isSignUp
                  ? 'Rejoins Connex et commence à partager'
                  : 'Bienvenue sur Connex'}
              </p>

              {/* Account type toggle */}
              {isSignUp && (
                <div className="flex gap-2 mb-4">
                  <button
                    type="button"
                    onClick={() => setIsCompany(false)}
                    className={`flex-1 flex items-center justify-center gap-2 px-3 py-2 rounded-lg font-medium transition-all text-sm ${
                      !isCompany
                        ? 'bg-primary text-primary-foreground'
                        : 'bg-muted text-muted-foreground hover:bg-muted/80'
                    }`}
                  >
                    <Users className="w-4 h-4" />
                    Utilisateur
                  </button>
                  <button
                    type="button"
                    onClick={() => setIsCompany(true)}
                    className={`flex-1 flex items-center justify-center gap-2 px-3 py-2 rounded-lg font-medium transition-all text-sm ${
                      isCompany
                        ? 'bg-primary text-primary-foreground'
                        : 'bg-muted text-muted-foreground hover:bg-muted/80'
                    }`}
                  >
                    <Building2 className="w-4 h-4" />
                    Entreprise
                  </button>
                </div>
              )}
            </div>

            {/* Form */}
            <form onSubmit={handleSubmit} className="space-y-4">
              {isSignUp && (
                <div>
                  <label className="block text-sm font-medium text-foreground mb-2">
                    {isCompany ? 'Nom de l\'entreprise' : 'Nom complet'}
                  </label>
                  <Input
                    type="text"
                    name="name"
                    placeholder={isCompany ? 'Acme Corporation' : 'Jean Dupont'}
                    value={formData.name}
                    onChange={handleChange}
                    required={isSignUp}
                    className="rounded-lg"
                  />
                </div>
              )}

              <div>
                <label className="block text-sm font-medium text-foreground mb-2">
                  Email
                </label>
                <Input
                  type="email"
                  name="email"
                  placeholder="toi@exemple.com"
                  value={formData.email}
                  onChange={handleChange}
                  required
                  className="rounded-lg"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-foreground mb-2">
                  Mot de passe
                </label>
                <Input
                  type="password"
                  name="password"
                  placeholder="••••••••"
                  value={formData.password}
                  onChange={handleChange}
                  required
                  className="rounded-lg"
                />
              </div>

              {isSignUp && (
                <div>
                  <label className="block text-sm font-medium text-foreground mb-2">
                    Confirmer le mot de passe
                  </label>
                  <Input
                    type="password"
                    name="confirmPassword"
                    placeholder="••••••••"
                    value={formData.confirmPassword}
                    onChange={handleChange}
                    required={isSignUp}
                    className="rounded-lg"
                  />
                </div>
              )}

              <Button
                type="submit"
                className="w-full rounded-lg h-10 mt-6"
                disabled={isLoading}
              >
                {isLoading
                  ? 'Chargement...'
                  : isSignUp
                    ? 'Créer un compte'
                    : 'Se connecter'}
              </Button>
            </form>

            {/* Divider */}
            <div className="relative my-6">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-border" />
              </div>
              <div className="relative flex justify-center text-sm">
                <span className="px-2 bg-background text-muted-foreground">
                  ou
                </span>
              </div>
            </div>

            {/* Social buttons */}
            <div className="space-y-3">
              <Button
                type="button"
                variant="outline"
                className="w-full rounded-lg"
                disabled
              >
                Continuer avec Google
              </Button>
              <Button
                type="button"
                variant="outline"
                className="w-full rounded-lg"
                disabled
              >
                Continuer avec GitHub
              </Button>
            </div>

            {/* Toggle sign up/in */}
            <div className="mt-6 text-center text-sm text-muted-foreground">
              {isSignUp ? (
                <>
                  Tu as déjà un compte?{' '}
                  <button
                    type="button"
                    onClick={() => setIsSignUp(false)}
                    className="text-primary hover:underline font-medium"
                  >
                    Se connecter
                  </button>
                </>
              ) : (
                <>
                  Tu n&apos;as pas de compte?{' '}
                  <button
                    type="button"
                    onClick={() => setIsSignUp(true)}
                    className="text-primary hover:underline font-medium"
                  >
                    Créer un compte
                  </button>
                </>
              )}
            </div>

            {/* Privacy link */}
            <p className="text-xs text-muted-foreground text-center mt-4">
              En {isSignUp ? 'créant un compte' : 'te connectant'}, tu acceptes nos{' '}
              <Link href="#" className="text-primary hover:underline">
                Conditions d&apos;utilisation
              </Link>{' '}
              et{' '}
              <Link href="#" className="text-primary hover:underline">
                Politique de confidentialité
              </Link>
            </p>
          </Card>

          {/* Demo notice */}
          <div className="mt-4 p-4 rounded-lg bg-muted/50 border border-border text-xs text-muted-foreground text-center">
            <p className="font-medium mb-1">Demo Mode</p>
            <p>Any email/password combination will work for this demo</p>
          </div>
        </div>
      </div>
    </main>
  )
}
