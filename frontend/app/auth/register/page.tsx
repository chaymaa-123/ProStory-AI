'use client';


import { Navigation } from '@/components/NavigationConn';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { Building2, Users } from 'lucide-react';
import { authService } from '@/services/authService';

export default function RegisterPage() {
  // --- ÉTATS ---
  const [isCompany, setIsCompany] = useState(false);
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
    name: '',
  });
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const router = useRouter();

  // --- GESTION DES INPUTS ---
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  // --- ENVOI AU BACKEND ---
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');

    try {
      // 1. Validation de sécurité locale
      if (formData.password !== formData.confirmPassword) {
        throw new Error("Les mots de passe ne correspondent pas.");
      }

      // 2. Appel au service Register (Vers FastAPI)
      await authService.register({
        name: formData.name,
        email: formData.email,
        password: formData.password,
        role: isCompany ? 'entreprise' : 'user'
      });

      // 3. Succès
      alert("Compte créé avec succès !");
      
      // Redirection vers la page de login (ou accueil selon votre flux)
      // Note: On utilise window.location si useRouter pose problème dans l'environnement de test
      if (router) {
        router.push('/auth/login'); 
      } else {
        window.location.href = '/auth/login';
      }
    } catch (err: any) {
      // On affiche l'erreur réelle renvoyée par le backend ou l'erreur locale
      setError(err.message || "Une erreur est survenue");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="min-h-screen flex flex-col bg-background">
      {/* Barre de navigation */}
      <Navigation currentPath="/auth/register" />

      <div className="flex-1 flex items-center justify-center px-4 py-12">
        <div className="w-full max-w-md">
          <Card className="p-8 shadow-lg border-muted">
            <div className="text-center mb-8">
              <h1 className="text-2xl font-bold text-foreground mb-4">
                Créer un compte
              </h1>
              <p className="text-sm text-muted-foreground mb-6">
                Rejoins ProStory-AI et commence à partager ton expérience.
              </p>

              {/* Sélecteur de type de compte (Utilisateur vs Entreprise) */}
              <div className="flex gap-2 mb-4">
                <button
                  type="button"
                  onClick={() => setIsCompany(false)}
                  className={`flex-1 flex items-center justify-center gap-2 px-3 py-2 rounded-lg font-medium transition-all text-sm border ${
                    !isCompany
                      ? 'bg-primary text-primary-foreground border-primary'
                      : 'bg-muted text-muted-foreground border-transparent hover:bg-muted/80'
                  }`}
                >
                  <Users className="w-4 h-4" />
                  Utilisateur
                </button>
                <button
                  type="button"
                  onClick={() => setIsCompany(true)}
                  className={`flex-1 flex items-center justify-center gap-2 px-3 py-2 rounded-lg font-medium transition-all text-sm border ${
                    isCompany
                      ? 'bg-primary text-primary-foreground border-primary'
                      : 'bg-muted text-muted-foreground border-transparent hover:bg-muted/80'
                  }`}
                >
                  <Building2 className="w-4 h-4" />
                  Entreprise
                </button>
              </div>
            </div>

            {/* Affichage des erreurs (Backend ou validation) */}
            {error && (
              <div className="mb-6 p-3 bg-red-50 border border-red-200 text-red-600 rounded-lg text-sm text-center font-medium">
                {error}
              </div>
            )}

            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-foreground mb-2">
                  {isCompany ? 'Nom de l\'entreprise' : 'Nom complet'}
                </label>
                <Input
                  type="text"
                  name="name"
                  placeholder={isCompany ? 'Ex: Story Corp' : 'Ex: Jean Dupont'}
                  value={formData.name}
                  onChange={handleChange}
                  required
                  className="rounded-lg h-11"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-foreground mb-2">
                  Email professionnel
                </label>
                <Input
                  type="email"
                  name="email"
                  placeholder="nom@exemple.com"
                  value={formData.email}
                  onChange={handleChange}
                  required
                  className="rounded-lg h-11"
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
                  className="rounded-lg h-11"
                />
              </div>

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
                  required
                  className="rounded-lg h-11"
                />
              </div>

              <Button
                type="submit"
                className="w-full rounded-lg h-11 mt-6 font-semibold text-white"
                disabled={isLoading}
              >
                {isLoading ? 'Traitement en cours...' : 'S\'inscrire maintenant'}
              </Button>
            </form>

            <div className="mt-6 text-center text-sm text-muted-foreground">
              Vous avez déjà un compte ?{' '}
              <Link href="/auth/login" className="text-primary hover:underline font-medium">
                Se connecter
              </Link>
            </div>

            <p className="text-xs text-muted-foreground text-center mt-6 leading-relaxed">
              En créant un compte, vous acceptez nos{' '}
              <Link href="#" className="text-primary hover:underline">Conditions d'utilisation</Link> et notre{' '}
              <Link href="#" className="text-primary hover:underline">Politique de confidentialité</Link>.
            </p>
          </Card>
        </div>
      </div>
    </main>
  );
}