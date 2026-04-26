'use client';

import { Navigation } from '@/components/Navigation';
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
    email: '', password: '', confirmPassword: '', name: '',
  });
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const router = useRouter();

  // --- LOGIQUE ---
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    if (formData.password !== formData.confirmPassword) {
      return setError("Les mots de passe ne correspondent pas.");
    }

    setIsLoading(true);
    try {
      // Appel au service d'inscription
      await authService.register({
        name: formData.name,
        email: formData.email,
        password: formData.password,
        role: isCompany ? 'entreprise' : 'user',
        company_name: isCompany ? formData.name : null
      });

      // REDIRECTION : Onboarding pour les users, Dashboard pour les pros
      router.push(isCompany ? '/dashboard' : '/formulaire');
    } catch (err: any) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="min-h-screen flex flex-col bg-background selection:bg-primary/20">
      <Navigation currentPath="/auth/register" />

      <div className="flex-1 flex items-center justify-center px-4 py-12">
        <Card className="w-full max-w-md p-8 shadow-2xl border-muted/50 rounded-3xl backdrop-blur-sm bg-card/80">
          <div className="text-center mb-8">
            <h1 className="text-3xl font-black tracking-tighter mb-2">Rejoins l'aventure</h1>
            <p className="text-sm text-muted-foreground">Crée ton profil ProStory-AI en quelques secondes.</p>

            {/* Sélecteur de rôle (Utilisateur / Entreprise) */}
            <div className="flex gap-3 mt-8 p-1 bg-muted/30 rounded-2xl">
              {[
                { id: 'user', label: 'Utilisateur', icon: Users, active: !isCompany },
                { id: 'company', label: 'Entreprise', icon: Building2, active: isCompany }
              ].map(role => (
                <button
                  key={role.id}
                  type="button"
                  onClick={() => setIsCompany(role.id === 'company')}
                  className={`flex-1 flex items-center justify-center gap-2 py-3 rounded-xl font-bold text-sm transition-all ${
                    role.active ? 'bg-background shadow-md text-primary scale-100' : 'text-muted-foreground hover:bg-muted/50 scale-[0.98]'
                  }`}
                >
                  <role.icon className="w-4 h-4" /> {role.label}
                </button>
              ))}
            </div>
          </div>

          {error && (
            <div className="mb-6 p-4 bg-red-500/10 border border-red-500/20 text-red-500 rounded-2xl text-xs font-bold text-center animate-in fade-in slide-in-from-top-2">
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            {/* Champs de saisie standard */}
            {[
               { name: 'name', label: isCompany ? 'Nom de la structure' : 'Ton nom complet', type: 'text', placeholder: 'Ex: Jean Story' },
               { name: 'email', label: 'Email Pro', type: 'email', placeholder: 'nom@exemple.com' },
               { name: 'password', label: 'Mot de passe', type: 'password', placeholder: '••••••••' },
               { name: 'confirmPassword', label: 'Vérification', type: 'password', placeholder: '••••••••' }
            ].map(field => (
              <div key={field.name} className="space-y-1.5">
                <label className="text-[10px] font-black uppercase tracking-widest text-muted-foreground ml-1">
                  {field.label}
                </label>
                <Input
                  name={field.name}
                  type={field.type}
                  placeholder={field.placeholder}
                  value={(formData as any)[field.name]}
                  onChange={handleChange}
                  required
                  className="rounded-xl h-12 bg-background/50 border-muted-foreground/10 focus:border-primary transition-all"
                />
              </div>
            ))}

            <Button type="submit" className="w-full h-12 rounded-xl font-black text-lg bg-primary hover:bg-primary/90 mt-4 transition-transform active:scale-95" disabled={isLoading}>
              {isLoading ? 'Création...' : 'C\'est parti !'}
            </Button>
          </form>

          <footer className="mt-8 pt-6 border-t border-muted/30 text-center">
            <p className="text-xs text-muted-foreground">
              Déjà un compte ? <Link href="/auth/login" className="text-primary font-black hover:underline underline-offset-4">Connecte-toi</Link>
            </p>
          </footer>
        </Card>
      </div>
    </main>
  );
}