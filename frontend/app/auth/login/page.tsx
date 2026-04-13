'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { LogIn, Mail, Lock, ArrowRight, Globe } from 'lucide-react';

// Importations relatives pour éviter les erreurs de résolution d'alias
import { Navigation } from '@/components/Navigation';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { authService } from '@/services/authService';

export default function LoginPage() {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const router = useRouter();

  // Gestion des changements dans les champs de saisie
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  // Envoi des identifiants au backend
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');

    try {
      // Appel au service de connexion
      const response = await authService.login({
        email: formData.email,
        password: formData.password,
      });

      // Redirection intelligente basée sur le rôle de l'utilisateur
      if (response.user.role === 'entreprise') {
        router.push('/dashboard');
      } else {
        router.push('/feed');
      }
    } catch (err: any) {
      // Affichage du message d'erreur (ex: "Identifiants incorrects")
      setError(err.message || "Impossible de se connecter. Vérifiez vos accès.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="min-h-screen flex flex-col bg-background">
      <Navigation currentPath="/auth/login" />

      <div className="flex-1 flex items-center justify-center px-4 py-12">
        <div className="w-full max-w-md">
          <Card className="p-8 shadow-lg border-muted">
            {/* Entête de la carte */}
            <div className="text-center mb-8">
              <div className="inline-flex items-center justify-center w-14 h-14 bg-blue-50 rounded-2xl mb-4 text-blue-600">
                <LogIn className="w-7 h-7" />
              </div>
              <h1 className="text-2xl font-bold text-foreground mb-4">Bienvenue</h1>
              <p className="text-sm text-muted-foreground mb-6">
                Connectez-vous pour accéder à votre espace ProStory-AI.
              </p>
            </div>

            {/* Affichage des erreurs de connexion */}
            {error && (
              <div className="mb-6 p-3 bg-red-50 border border-red-100 text-red-600 rounded-lg text-sm text-center font-medium animate-in fade-in slide-in-from-top-1">
                {error}
              </div>
            )}

            <form onSubmit={handleSubmit} className="space-y-5">
              {/* Champ Email */}
              <div className="space-y-1.5">
                <label className="text-xs font-bold uppercase text-gray-400 ml-1">
                  Email professionnel
                </label>
                <div className="relative">
                  <Mail className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
                  <Input
                    type="email"
                    name="email"
                    placeholder="nom@exemple.com"
                    value={formData.email}
                    onChange={handleChange}
                    required
                    className="pl-10 h-11 border-gray-200 focus:border-blue-500 rounded-xl"
                  />
                </div>
              </div>

              {/* Champ Mot de passe */}
              <div className="space-y-1.5">
                <div className="flex justify-between items-center">
                  <label className="text-xs font-bold uppercase text-gray-400 ml-1">
                    Mot de passe
                  </label>
                  <Link href="#" className="text-xs font-medium text-blue-600 hover:underline">
                    Oublié ?
                  </Link>
                </div>
                <div className="relative">
                  <Lock className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
                  <Input
                    type="password"
                    name="password"
                    placeholder="••••••••"
                    value={formData.password}
                    onChange={handleChange}
                    required
                    className="pl-10 h-11 border-gray-200 focus:border-blue-500 rounded-xl"
                  />
                </div>
              </div>

              {/* Bouton de validation */}
              <Button
                type="submit"
                className="w-full h-12 mt-6 text-white font-bold rounded-xl shadow-md shadow-blue-200"
                disabled={isLoading}
              >
                {isLoading ? (
                  <span className="flex items-center gap-2">
                    <span className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
                    Vérification...
                  </span>
                ) : (
                  <span className="flex items-center gap-2">
                    Se connecter <ArrowRight className="w-4 h-4" />
                  </span>
                )}
              </Button>
            </form>

            {/* Pied de carte : Inscription */}
            <div className="mt-10 pt-6 border-t border-gray-100 text-center">
              <p className="text-sm text-gray-500">
                Pas encore de compte ?{' '}
                <Link href="/auth/register" className="text-blue-600 font-bold hover:underline">
                  S'inscrire gratuitement
                </Link>
              </p>
            </div>
          </Card>

          {/* Note de sécurité */}
          <div className="mt-8 text-center">
            <p className="text-xs text-gray-400 flex items-center justify-center gap-2">
              <Globe className="w-3 h-3" /> Plateforme sécurisée par ProStory-AI
            </p>
          </div>
        </div>
      </div>
    </main>
  );
}