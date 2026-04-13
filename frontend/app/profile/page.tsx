'use client';

import React, { useState, useEffect, ChangeEvent, FormEvent } from 'react';
import { 
  User, 
  Mail, 
  Shield, 
  Camera, 
  Save, 
  Settings, 
  Bell, 
  Lock,
  CheckCircle,
  Trash2
} from 'lucide-react';

import { Navigation } from '@/components/Navigation';
import { Button } from '@/components/ui/button';
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';

interface ProfileInputProps {
  label: string;
  icon: any;
  value: string;
  disabled?: boolean;
  onChange?: (e: ChangeEvent<HTMLInputElement>) => void;
  name: string;
  type?: string;
}

/**
 * COMPOSANT LOCAL : Input de profil stylisé utilisant shadcn
 */
const ProfileInput = ({ label, icon: Icon, value, disabled = false, onChange, name, type = "text" }: ProfileInputProps) => (
  <div className="space-y-2">
    <Label htmlFor={name} className="text-xs font-bold uppercase tracking-wider text-muted-foreground ml-1">
      {label}
    </Label>
    <div className="relative group">
      <div className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground group-focus-within:text-primary transition-colors">
        <Icon className="w-4 h-4" />
      </div>
      <Input
        id={name}
        type={type}
        name={name}
        value={value}
        onChange={onChange}
        disabled={disabled}
        className="pl-10 rounded-xl"
      />
    </div>
  </div>
);

export default function ProfilePage() {
  const [mounted, setMounted] = useState(false);
  const [user, setUser] = useState({ name: '', email: '', role: '' });
  const [isSaving, setIsSaving] = useState(false);
  const [showSuccess, setShowSuccess] = useState(false);

  useEffect(() => {
    setMounted(true);
    const savedUser = localStorage.getItem('user');
    if (savedUser) {
      try {
        const parsed = JSON.parse(savedUser);
        if (parsed) {
          setUser({
            name: parsed.name || '',
            email: parsed.email || '',
            role: parsed.role || ''
          });
        }
      } catch (e) {
        console.error("Erreur de lecture du profil", e);
      }
    }
  }, []);

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setUser(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSave = async (e: FormEvent) => {
    e.preventDefault();
    setIsSaving(true);
    
    try {
      // Simulation d'appel API
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Mise à jour locale
      localStorage.setItem('user', JSON.stringify(user));
      
      setShowSuccess(true);
      setTimeout(() => setShowSuccess(false), 3000);
    } catch (err) {
      console.error("Erreur d'enregistrement", err);
    } finally {
      setIsSaving(false);
    }
  };

  if (!mounted) return null;


  return (
    <div className="min-h-screen bg-background flex flex-col font-sans">
      <Navigation currentPath="/profile" />

      <main className="flex-1 max-w-5xl mx-auto w-full px-4 pt-12 pb-20">
        <div className="grid grid-cols-1 md:grid-cols-12 gap-8">
          
          {/* Colonne de gauche : Avatar et Navigation Profil */}
          <div className="md:col-span-4 space-y-6">
            <Card className="text-center overflow-hidden border-border/50">
              <CardContent className="pt-8 pb-6">
                <div className="relative inline-block mb-4">
                  <div className="w-24 h-24 rounded-full bg-gradient-to-br from-primary to-accent flex items-center justify-center text-white text-3xl font-black shadow-xl">
                    {user.name ? user.name[0] : '?'}
                  </div>
                  <Button size="icon" variant="secondary" className="absolute bottom-0 right-0 rounded-full w-8 h-8 shadow-lg border border-border hover:scale-110 transition-transform">
                    <Camera className="w-4 h-4" />
                  </Button>
                </div>
                <h2 className="font-bold text-xl text-foreground">{user.name || "Utilisateur"}</h2>
                <p className="text-xs font-bold text-primary uppercase tracking-widest mt-1">
                  {user.role || "Rôle inconnu"}
                </p>
                
                <div className="mt-8 pt-6 border-t border-border/50 space-y-4">
                  <div className="flex items-center justify-between text-xs font-semibold">
                    <span className="text-muted-foreground uppercase">Statut Compte</span>
                    <span className="text-green-500 flex items-center gap-1.5 font-bold">
                      <CheckCircle className="w-3.5 h-3.5" /> Vérifié
                    </span>
                  </div>
                  <div className="flex items-center justify-between text-xs font-semibold">
                    <span className="text-muted-foreground uppercase">Membre depuis</span>
                    <span className="text-foreground">Avril 2026</span>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Menu de navigation profil */}
            <Card className="border-border/50 overflow-hidden">
              <div className="flex flex-col">
                <button className="flex items-center justify-start gap-3 px-6 py-4 text-sm font-bold text-primary bg-primary/5 border-l-4 border-primary transition-all">
                  <User className="w-4 h-4" /> Informations
                </button>
                <button className="flex items-center justify-start gap-3 px-6 py-4 text-sm font-bold text-muted-foreground hover:bg-muted/50 hover:text-foreground transition-all">
                  <Bell className="w-4 h-4" /> Notifications
                </button>
                <button className="flex items-center justify-start gap-3 px-6 py-4 text-sm font-bold text-muted-foreground hover:bg-muted/50 hover:text-foreground transition-all">
                  <Lock className="w-4 h-4" /> Sécurité
                </button>
                <button className="flex items-center justify-start gap-3 px-6 py-4 text-sm font-bold text-muted-foreground hover:bg-muted/50 hover:text-foreground transition-all">
                  <Settings className="w-4 h-4" /> Paramètres
                </button>
              </div>
            </Card>
          </div>

          {/* Colonne de droite : Formulaire */}
          <div className="md:col-span-8 space-y-6">
            <Card className="border-border/50">
              <CardHeader className="pb-8">
                <CardTitle className="text-2xl font-bold">Informations Générales</CardTitle>
                <CardDescription>Mettez à jour vos informations personnelles pour personnaliser votre expérience.</CardDescription>
              </CardHeader>
              
              <CardContent>
                {showSuccess && (
                  <div className="mb-8 p-4 bg-green-500/10 border border-green-500/20 text-green-600 dark:text-green-400 rounded-2xl flex items-center gap-3 text-sm font-bold animate-in fade-in slide-in-from-top-2">
                    <CheckCircle className="w-5 h-5" />
                    Profil mis à jour avec succès !
                  </div>
                )}

                <form onSubmit={handleSave} className="space-y-8">
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-8">
                    <ProfileInput
                      label="Nom Complet"
                      name="name"
                      icon={User}
                      value={user.name}
                      onChange={handleChange}
                    />
                    <ProfileInput
                      label="Rôle Plateforme"
                      name="role"
                      icon={Shield}
                      value={user.role}
                      disabled={true}
                    />
                  </div>

                  <ProfileInput
                    label="Adresse Email Professionnelle"
                    name="email"
                    icon={Mail}
                    value={user.email}
                    disabled={true}
                  />

                  <div className="pt-8 border-t border-border/50 flex flex-col sm:flex-row items-center justify-between gap-6">
                    <p className="text-[10px] text-muted-foreground font-bold uppercase max-w-[280px] leading-relaxed">
                      Note : L'adresse email et le rôle sont liés à votre inscription initiale et ne sont pas modifiables.
                    </p>
                    <Button
                      type="submit"
                      disabled={isSaving}
                      className="w-full sm:w-auto px-10 py-6 rounded-2xl font-bold text-base shadow-lg shadow-primary/20 active:scale-95 transition-all"
                    >
                      {isSaving ? (
                        <span className="flex items-center gap-2">
                          <span className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                          Enregistrement...
                        </span>
                      ) : (
                        <span className="flex items-center gap-2">
                          <Save className="w-4 h-4" />
                          Enregistrer les modifications
                        </span>
                      )}
                    </Button>
                  </div>
                </form>
              </CardContent>
            </Card>

            {/* Zone de danger */}
            <Card className="border-red-500/20 bg-red-500/5 overflow-hidden">
              <CardHeader>
                <CardTitle className="text-sm font-bold text-red-600 flex items-center gap-2">
                  <Trash2 className="w-4 h-4" /> Zone de danger
                </CardTitle>
                <CardDescription className="text-red-600/70 font-medium">
                  La suppression de votre compte est irréversible. Toutes vos données seront effacées.
                </CardDescription>
              </CardHeader>
              <CardFooter className="pt-2">
                <button className="text-xs font-bold text-red-600 hover:underline underline-offset-4">
                  Supprimer mon compte définitivement
                </button>
              </CardFooter>
            </Card>
          </div>
        </div>
      </main>
    </div>
  );
}