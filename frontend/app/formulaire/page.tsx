'use client';

import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import {
    User, Sparkles, Target, Briefcase, MapPin,
    ChevronRight, ChevronLeft, Check, Plus, X,
    Building2, Hash, Zap, Heart, Globe, Award
} from 'lucide-react';
import { Navigation } from '@/components/Navigation';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Badge } from '@/components/ui/badge';
import { cn } from '@/lib/utils';

// --- SUGGESTIONS DE DATA ---
const SUGGESTED_SKILLS = [
    "React", "Node.js", "Python", "UI/UX Design", "Figma",
    "Gestion de Projet", "DevOps", "AI / ML", "Marketing", "Data Science",
    "SQL", "JavaScript", "Agile", "TypeScript", "Public Speaking"
];

const SUGGESTED_PREFS = [
    "Télétravail", "Collaboration", "Innovation", "Flexibilité",
    "Projets Sociaux", "Open Source", "Leadership", "Start-up Spirit",
    "Environnement Calme", "Équité", "Formation Continue"
];

const STATUS_OPTIONS = [
    { value: 'etudiant', label: 'Étudiant' },
    { value: 'stagiaire', label: 'Stagiaire' },
    { value: 'employé', label: 'Employé' },
    { value: 'freelance', label: 'Freelance' },
    { value: 'RH', label: 'RH / Recruteur' },
    { value: 'entreprise', label: 'Chef d\'entreprise' }
];

const SUGGESTED_PAINS = [
    "Micromanagement", "Réunions Inutiles", "Burnout", "Manque de Vision",
    "Outils Obsolètes", "Silos", "Processus Rigides", "Manque de feedback"
];

export default function PremiumOnboarding() {
    const router = useRouter();
    const [step, setStep] = useState(1);
    const [mounted, setMounted] = useState(false);
    const [authData, setAuthData] = useState({ userId: '', token: '' });

    // DONNÉES DU FORMULAIRE
    const [formData, setFormData] = useState({
        nom: '', prenom: '', age: '', ville: '',
        statut: '', domaine_activite: '', poste_actuel: '', nom_entreprise: '',
        bio: '', competences: [] as string[],
        env_travail_prefere: [] as string[],
        points_de_douleur: [] as string[],
    });

    const [tempTags, setTempTags] = useState({ skill: '', pref: '', pain: '' });

    useEffect(() => {
        setMounted(true);
        const user = JSON.parse(localStorage.getItem('user') || '{}');
        const token = localStorage.getItem('token');

        if (user.role === 'entreprise') {
            router.push('/dashboard');
        } else if (user.id && token) {
            setAuthData({ userId: user.id, token });
        }
    }, [router]);

    // LOGIQUE GESTION TAGS
    const addTag = (field: 'competences' | 'env_travail_prefere' | 'points_de_douleur', tag: string) => {
        if (tag.trim() && !formData[field].includes(tag.trim())) {
            setFormData({ ...formData, [field]: [...formData[field], tag.trim()] });
        }
    };

    const removeTag = (field: 'competences' | 'env_travail_prefere' | 'points_de_douleur', tag: string) => {
        setFormData({ ...formData, [field]: formData[field].filter(t => t !== tag) });
    };

    const handleSubmit = async () => {
        try {
            // Nettoyage : On transforme les "" en null pour satisfaire la DB
            const cleanedData = Object.fromEntries(
                Object.entries(formData).map(([key, value]) => [
                    key, 
                    (typeof value === 'string' && value.trim() === '') ? null : value
                ])
            );

            const payload = { 
                ...cleanedData, 
                age: parseInt(formData.age) || null, 
                is_onboarding_complete: true 
            };
            
            console.log("SENDING CLEANED PROFILE DATA:", payload);
            
            const res = await fetch(`http://localhost:8000/api/auth/profile/update/${authData.userId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authData.token}`
                },
                body: JSON.stringify(payload)
            });

            if (res.ok) {
                const user = JSON.parse(localStorage.getItem('user') || '{}');
                localStorage.setItem('user', JSON.stringify({ ...user, is_onboarding_complete: true }));
                router.push('/feed');
            }
        } catch (err) {
            console.error("Erreur de sauvegarde", err);
        }
    };

    if (!mounted) return null;

    return (
        <div className="min-h-screen bg-[#020202] text-white selection:bg-primary/30 font-sans overflow-x-hidden">
            <Navigation currentPath="/formulaire" />

            {/* Background Decor */}
            <div className="fixed top-0 left-0 w-full h-full -z-10 bg-[radial-gradient(circle_at_50%_0%,_#1a1a2e_0%,_transparent_50%)]" />
            <div className="fixed bottom-0 right-0 w-[500px] h-[500px] bg-primary/5 rounded-full blur-[150px] -z-10" />

            <main className="max-w-4xl mx-auto px-4 pt-12 pb-32 space-y-8 animate-in fade-in duration-1000">

                {/* PROGRESS SYSTEM */}
                <div className="flex flex-col gap-4 mb-16">
                    <div className="flex justify-between items-end">
                        <div className="space-y-1">
                            <p className="text-[10px] font-black uppercase tracking-[0.4em] text-primary">Onboarding Initial</p>
                            <h1 className="text-4xl font-black tracking-tighter">Étape {step} sur 3</h1>
                        </div>
                        <p className="text-white/40 text-xs font-bold">{Math.round((step / 3) * 100)}% Complété</p>
                    </div>
                    <div className="h-1.5 w-full bg-white/5 rounded-full overflow-hidden">
                        <div className="h-full bg-primary transition-all duration-700 ease-out" style={{ width: `${(step / 3) * 100}%` }} />
                    </div>
                </div>

                <Card className="p-0 border-white/5 bg-white/[0.02] backdrop-blur-2xl rounded-[3rem] shadow-[0_32px_64px_-16px_rgba(0,0,0,0.6)] overflow-hidden">

                    <div className="p-10 md:p-16 space-y-12 min-h-[500px]">

                        {/* STEP 1 : IDENTITÉ */}
                        {step === 1 && (
                            <div className="space-y-10 animate-in slide-in-from-right duration-500">
                                <div className="space-y-2">
                                    <h2 className="text-3xl md:text-5xl font-black tracking-tighter">Commençons par toi...</h2>
                                    <p className="text-white/40 text-lg font-medium">Pour te proposer les meilleures opportunités.</p>
                                </div>

                                <div className="grid grid-cols-1 md:grid-cols-2 gap-8 pt-4">
                                    <PremiumInput label="Prénom" value={formData.prenom} icon={User} onChange={(v: string) => setFormData({ ...formData, prenom: v })} placeholder="Ex: Jean" />
                                    <PremiumInput label="Nom" value={formData.nom} icon={User} onChange={(v: string) => setFormData({ ...formData, nom: v })} placeholder="Ex: Story" />
                                    <PremiumInput label="Âge" value={formData.age} icon={Hash} onChange={(v: string) => setFormData({ ...formData, age: v })} placeholder="Ex: 28" type="number" />
                                    <PremiumInput label="Ville" value={formData.ville} icon={MapPin} onChange={(v: string) => setFormData({ ...formData, ville: v })} placeholder="Ex: Paris" />
                                </div>
                            </div>
                        )}

                        {/* STEP 2 : VIE PROFESSIONNELLE & ENTREPRISE */}
                        {step === 2 && (
                            <div className="space-y-10 animate-in slide-in-from-right duration-500">
                                <div className="space-y-2">
                                    <h2 className="text-3xl md:text-5xl font-black tracking-tighter">Ton Univers Pro</h2>
                                    <p className="text-white/40 text-lg font-medium">Où travailles-tu et que sais-tu faire ?</p>
                                </div>

                                <div className="grid grid-cols-1 md:grid-cols-2 gap-8 pt-4">
                                    <PremiumInput label="Poste Actuel" value={formData.poste_actuel} icon={Briefcase} onChange={(v: string) => setFormData({ ...formData, poste_actuel: v })} placeholder="Ex: Développeur Fullstack" />
                                    <PremiumInput label="Domaine d'activité" value={formData.domaine_activite} icon={Globe} onChange={(v: string) => setFormData({ ...formData, domaine_activite: v })} placeholder="Ex: Tech, Design, Santé..." />
                                    <PremiumInput label="Entreprise / École actuelle" value={formData.nom_entreprise} icon={Building2} onChange={(v: string) => setFormData({ ...formData, nom_entreprise: v })} placeholder="Ex: Google, Sorbonne..." />
                                </div>

                                {/* SÉLECTION DU STATUT */}
                                <div className="space-y-4 pt-4">
                                    <label className="text-[10px] font-black uppercase tracking-widest text-primary">Ton Statut Actuel</label>
                                    <div className="flex flex-wrap gap-3">
                                        {STATUS_OPTIONS.map(s => (
                                            <button
                                                key={s.value}
                                                type="button"
                                                onClick={() => setFormData({ ...formData, statut: s.value })}
                                                className={cn(
                                                    "px-6 py-3 rounded-2xl text-xs font-bold border transition-all active:scale-95",
                                                    formData.statut === s.value
                                                        ? "bg-primary border-primary text-black shadow-[0_0_20px_rgba(var(--primary),0.3)]"
                                                        : "bg-white/5 border-white/5 text-white/40 hover:bg-white/10 hover:text-white"
                                                )}
                                            >
                                                {s.label}
                                            </button>
                                        ))}
                                    </div>
                                    {!formData.statut && (
                                        <p className="text-[9px] text-white/20 italic">Veuillez sélectionner un statut système (sans accents pour la base de données).</p>
                                    )}
                                </div>

                                <div className="space-y-6 pt-4">
                                    <label className="text-[10px] font-black uppercase tracking-widest text-primary">Tes Compétences (Sélectionne ou ajoute)</label>
                                    <TagCloud
                                        suggestions={SUGGESTED_SKILLS}
                                        selected={formData.competences}
                                        onSelect={(t: string) => addTag('competences', t)}
                                        onRemove={(t: string) => removeTag('competences', t)}
                                        tempValue={tempTags.skill}
                                        onTempChange={(v: string) => setTempTags({ ...tempTags, skill: v })}
                                        onAddCustom={() => addTag('competences', tempTags.skill)}
                                    />
                                </div>
                            </div>
                        )}

                        {/* STEP 3 : ADN & BIO */}
                        {step === 3 && (
                            <div className="space-y-10 animate-in slide-in-from-right duration-500">
                                <div className="space-y-2">
                                    <h2 className="text-3xl md:text-5xl font-black tracking-tighter">Ton ADN de Travail</h2>
                                    <p className="text-white/40 text-lg font-medium">Ce qui te motive vraiment au quotidien.</p>
                                </div>

                                <div className="space-y-4 pt-4">
                                    <label className="text-[10px] font-black uppercase tracking-widest text-primary">Ta Biographie Pro</label>
                                    <Textarea
                                        value={formData.bio}
                                        onChange={e => setFormData({ ...formData, bio: e.target.value })}
                                        placeholder="Raconte-nous ton parcours en quelques phrases marquantes..."
                                        className="rounded-[2rem] min-h-[160px] bg-white/5 border-white/10 p-6 text-lg focus:border-primary transition-all text-white"
                                    />
                                </div>

                                <div className="grid grid-cols-1 md:grid-cols-2 gap-10">
                                    <div className="space-y-6">
                                        <label className="text-[10px] font-black uppercase tracking-widest text-green-400">Ce que tu adores</label>
                                        <TagCloud
                                            suggestions={SUGGESTED_PREFS}
                                            selected={formData.env_travail_prefere}
                                            onSelect={(t: string) => addTag('env_travail_prefere', t)}
                                            onRemove={(t: string) => removeTag('env_travail_prefere', t)}
                                            tempValue={tempTags.pref}
                                            onTempChange={(v: string) => setTempTags({ ...tempTags, pref: v })}
                                            onAddCustom={() => addTag('env_travail_prefere', tempTags.pref)}
                                        />
                                    </div>
                                    <div className="space-y-6">
                                        <label className="text-[10px] font-black uppercase tracking-widest text-rose-500">Ce que tu évites</label>
                                        <TagCloud
                                            suggestions={SUGGESTED_PAINS}
                                            selected={formData.points_de_douleur}
                                            onSelect={(t: string) => addTag('points_de_douleur', t)}
                                            onRemove={(t: string) => removeTag('points_de_douleur', t)}
                                            tempValue={tempTags.pain}
                                            onTempChange={(v: string) => setTempTags({ ...tempTags, pain: v })}
                                            onAddCustom={() => addTag('points_de_douleur', tempTags.pain)}
                                        />
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>

                    {/* CONTROL BAR */}
                    <div className="px-10 md:px-16 py-10 bg-white/[0.05] border-t border-white/5 flex justify-between items-center group">
                        {step > 1 ? (
                            <Button variant="ghost" className="rounded-2xl h-14 px-8 font-black gap-2 text-white/40 hover:text-white" onClick={() => setStep(step - 1)}>
                                <ChevronLeft className="w-5 h-5" /> RETOUR
                            </Button>
                        ) : <div />}

                        {step < 3 ? (
                            <Button disabled={!isStepReady(step, formData)} className="rounded-2xl h-14 px-12 bg-white text-black hover:bg-white/90 font-black gap-2 transition-transform active:scale-95 shadow-2xl" onClick={() => setStep(step + 1)}>
                                CONTINUER <ChevronRight className="w-5 h-5" />
                            </Button>
                        ) : (
                            <Button className="rounded-2xl h-14 px-12 bg-primary hover:bg-primary/90 font-black gap-2 transition-all active:scale-95 shadow-[0_10px_30px_-10px_rgba(var(--primary),0.5)]" onClick={handleSubmit}>
                                TERMINER MON ADN <Sparkles className="w-5 h-5" />
                            </Button>
                        )}
                    </div>
                </Card>
            </main>
        </div>
    );
}

// --- SOUS-COMPOSANTS PREMIUM ---

const PremiumInput = ({ label, value, icon: Icon, onChange, placeholder, type = "text" }: any) => (
    <div className="space-y-3">
        <label className="text-[10px] font-black uppercase tracking-widest text-white/30 ml-1">{label}</label>
        <div className="relative group">
            <div className="absolute left-4 top-1/2 -translate-y-1/2 text-white/20 group-focus-within:text-primary transition-colors">
                <Icon className="w-5 h-5" />
            </div>
            <Input
                type={type}
                value={value}
                onChange={e => onChange(e.target.value)}
                placeholder={placeholder}
                className="rounded-2xl h-14 pl-12 bg-white/5 border-white/10 text-white focus:border-primary transition-all placeholder:text-white/10"
            />
        </div>
    </div>
);

const TagCloud = ({ suggestions, selected, onSelect, onRemove, tempValue, onTempChange, onAddCustom }: any) => {
    return (
        <div className="space-y-4">
            {/* Input de saisie manuelle */}
            <div className="flex gap-2">
                <Input
                    value={tempValue}
                    onChange={e => onTempChange(e.target.value)}
                    onKeyDown={e => e.key === 'Enter' && (onAddCustom(), onTempChange(''))}
                    placeholder="Ajouter manuellement..."
                    className="rounded-xl h-10 bg-white/5 border-white/5 text-xs text-white"
                />
                <Button size="icon" className="h-10 w-10 rounded-xl" onClick={() => (onAddCustom(), onTempChange(''))}>
                    <Plus className="w-4 h-4" />
                </Button>
            </div>

            {/* Tags déjà sélectionnés */}
            <div className="flex flex-wrap gap-2 pt-2">
                {selected.map((tag: string) => (
                    <Badge key={tag} className="bg-primary/20 text-primary border-primary/20 py-1.5 px-3 rounded-xl flex items-center gap-2 group">
                        {tag}
                        <X className="w-3 h-3 cursor-pointer opacity-40 hover:opacity-100" onClick={() => onRemove(tag)} />
                    </Badge>
                ))}
            </div>

            {/* Suggestions cliquables */}
            <div className="flex flex-wrap gap-2 pt-4 border-t border-white/5">
                <p className="w-full text-[9px] font-black uppercase tracking-widest text-white/20 mb-1">Suggestions :</p>
                {suggestions.filter((s: string) => !selected.includes(s)).map((tag: string) => (
                    <button
                        key={tag}
                        onClick={() => onSelect(tag)}
                        className="text-[10px] font-bold px-3 py-1.5 rounded-xl border border-white/5 bg-white/5 text-white/40 hover:bg-white/10 hover:text-white transition-all active:scale-95"
                    >
                        + {tag}
                    </button>
                ))}
            </div>
        </div>
    );
};

// --- VALIDATION ÉTAPES ---
const isStepReady = (step: number, data: any) => {
    if (step === 1) return data.nom && data.prenom && data.age && data.ville;
    if (step === 2) return data.poste_actuel && data.domaine_activite && data.nom_entreprise && data.statut && data.competences.length > 0;
    return true;
};